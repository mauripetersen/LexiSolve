@echo off

echo activating virtual environment...
call .venv\Scripts\activate.bat
echo Done.
echo.

echo creating .exe...
call pyinstaller main.spec
echo Done.
echo.

echo deactivating virtual environment...
call .venv\Scripts\deactivate.bat
echo Done.
echo.
pause
