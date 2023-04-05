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