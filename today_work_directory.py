import os
import shutil
import configparser
import ast


PROGRAM_VERSION = "1.0.0"

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


def main():
    print(f"Program version: {PROGRAM_VERSION}")
    load_config()
    print(f"Current configuration: \n{config}")

    


if __name__ == "__main__":
    main()

