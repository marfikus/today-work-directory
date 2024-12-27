
# Today Work Directory

Маленькая утилита, которая делает следующее: по указанному пути создаёт новый каталог, имя которого представляет собой сегодняшнюю дату в формате `dd.mm.yy`. Дополнительно может открыть этот каталог в проводнике и добавить строку с сегодняшней датой и днем недели в буфер обмена.

Конфигурация утилиты выполняется в файле **today_work_directory.ini**.  
Параметры файла конфигурации:  
`path` - строка. Путь, по которому нужно создать каталог.  
`open_directory` - целое число (1 или 0). Открыть созданный каталог в проводнике. 1 - включено, 0 - выключено.  
`copy_date_to_clipboard` - целое число (1 или 0). Добавить строку с сегодняшней датой и днем недели в буфер обмена. 1 - включено, 0 - выключено.  
`debug_print` - целое число (1 или 0). Вывод различной отладочной информации в консоль. 1 - включено, 0 - выключено.

Скачать EXE-файл утилиты можно [здесь](https://github.com/marfikus/today-work-directory/releases/). Собирал через [Auto PY to EXE](https://pypi.org/project/auto-py-to-exe/).
