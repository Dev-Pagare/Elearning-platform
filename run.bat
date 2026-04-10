@echo off
echo ========================================
echo    E-Learning Django Server Starting...
echo ========================================
echo.

cd /d "%~dp0"

if exist "venv_new\Scripts\python.exe" (
    echo [OK] Using project virtual environment...
    venv_new\Scripts\python.exe manage.py runserver
) else (
    echo [INFO] venv_new not found, using system Python...
    python manage.py runserver
)

pause
