# GetExchRate

Если при утановки или обновлении poetry, возникла ошибка типа "The currently activated Python version 3.10.9 
is not supported by the project (3.10.10). Trying to find and use a compatible version.", то имеете дело с конфликтом
версий Python.
У меня на компьтере активизированная версия python 3.10.9, а проект поддерживает версию python 3.10.10. 
Чтобы это исправить, следует в файле pyproject.toml в python dependencies изменить версию python 
(pyproject.toml -> [tool.poetry.dependencies] -> python = "3.10.9").
Если проект поддерживает версию 3.10.9, а компьютер 3.10.10, то следует в файле pyproject.toml в python dependencies 
изменить версию python (pyproject.toml -> [tool.poetry.dependencies] -> python = "3.10.10").
Чтобы избежать подобных ситуаций нужно установить себе python той версии, которая указана здесь 
pyproject.toml -> [tool.poetry.dependencies] -> python = "...".

После установки Docker на ПК и его открытия, возникла ошибка "An unexpected error occurred". Это означает, 
что виртуализация должна быть включена в BIOS. Чтобы добавить виртуализацию в BIOS из Windows, нужно 
1. Нажмите кнопку меню «Пуск»; 
2. Выберите значок «Параметры \ Настройки» в левой части меню, чтобы открыть окно настроек; 
3. В окне «Параметры \ Настройки» выберите «Обновление и безопасность»;
4. Выберите «Восстановление» , затем «Перезагрузить сейчас»;
5. Меню «Параметры» появится после выполнения описанных выше процедур. Щелкните "Поиск и устранениие неисправностей".
6. Выберите "Дополнительные параметры".
7. Щелкните "Параметры встроенного ПО UEFI", затем выберите "Перезагрузить".
8. Отобразится интерфейс утилиты настройки BIOS.
9. Перейдите в Configuration -> Intel Virtual Technology -> ставим Enabled.
Если после проделанной работы при открытии Docker возникла ошибка "Docker requires a newer WSL kernel version"
(обновить WSL ядро), следует зайти через cmd в папку репозитория и запустить команду "wsl --update".
Если после команд docker compose build && docker compose up (запуска и сбора сборки) появляется ошибка вида 
"RUN poetry env use "3.10.10"", это значит, что этот файл использует poetry, чтобы создать окружение и тд. 
Если версии не совпадают - ошибка. Когда запускаем сборку docker compose build, то docker берёт образы python 
другой версии. Нужно исправить версию в образе docker. Версия python может быть настроена в следующих файлах:
- services/webapp/Dockerfile
- services/webapp/.python-version
- docker-compose.yml
- .env.dist
- .env
Если в этих файлах есть PYTHON_VERSION = "...", то исправляем на ту, которая установлена на вашем ПК.