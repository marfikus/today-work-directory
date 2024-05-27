import os
import configparser
import ast
import time
import locale
# import pyperclip
import subprocess


PROGRAM_VERSION = "1.1.0"

CONFIG_FILE = "today_work_directory.ini"
DEFAULT_CONFIG = {
    "path": "test/",
    "open_directory": True,
    "copy_date_to_clipboard": True,
    "debug_print": True,
}
config = {}

def load_config():
    global config

    def load_key(parser, key, type="str"):
        try:
            if type == "str":
                value = parser["DEFAULT"][key]
            elif type == "int":
                value = int(parser["DEFAULT"][key])
            elif type == "float":
                value = float(parser["DEFAULT"][key])
            elif type == "bool":
                value = bool(int(parser["DEFAULT"][key]))
            elif type == "list":
                value = ast.literal_eval(parser["DEFAULT"][key])
        except KeyError:
            print(f"No key '{key}' in config file! Loaded from DEFAULT_CONFIG")
            value = DEFAULT_CONFIG[key]

        return value


    if not os.path.exists(CONFIG_FILE):
        print("Config file not found! Loaded DEFAULT_CONFIG")
        config = DEFAULT_CONFIG
        return

    parser = configparser.ConfigParser()
    parser.read(CONFIG_FILE, encoding="utf-8")

    config["path"] = load_key(parser, "path", "str")
    config["open_directory"] = load_key(parser, "open_directory", "bool")
    config["copy_date_to_clipboard"] = load_key(parser, "copy_date_to_clipboard", "bool")
    config["debug_print"] = load_key(parser, "debug_print", "bool")


def debug_print(msg):
    if config["debug_print"]:
        print(msg)


# from: https://stackoverflow.com/questions/11063458/python-script-to-copy-text-to-clipboard/41029935#41029935
def copy2clip(txt):
    cmd = "echo " + txt.strip() + "|clip"
    return subprocess.check_call(cmd, shell=True)


def main():
    print(f"Program version: {PROGRAM_VERSION}")
    load_config()
    print(f"Current configuration: \n{config}")

    locale.setlocale(locale.LC_ALL, "Russian_Russia.1251")

    date = time.strftime("%d.%m.%y")
    week_day = time.strftime("%a")
    full_date = f"{date} {week_day}"
    debug_print(full_date)

    if config["copy_date_to_clipboard"]:
        # pyperclip.copy(full_date)
        copy2clip(full_date)

    if not os.path.exists(config["path"]):
        print(f"Path '{config['path']}' is not exists!")
        return

    dir_path = os.path.join(config["path"], date)
    dir_path = os.path.normpath(dir_path)
    debug_print(f"dir_path: '{dir_path}'")

    if os.path.exists(dir_path):
        print(f"Path '{dir_path}' is already exists!")
    else:
        try:
            os.mkdir(dir_path)
        except Exception as er:
            print(er)
            return

    if config["open_directory"]:
        subprocess.Popen(f"explorer {dir_path}")


if __name__ == "__main__":
    main()

