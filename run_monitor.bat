@echo off
:: Set email configuration - Replace with your actual values
set EMAIL_SENDER=your_email@gmail.com
set EMAIL_PASSWORD=your_16_char_app_password
set EMAIL_RECEIVER=recipient_email@gmail.com

:: Set project directory to the batch file's location
set PROJECT_DIR=%~dp0

:: Change to project directory
cd /d "%PROJECT_DIR%"

:: Set paths
set PYTHON_EXE=%PROJECT_DIR%venv\Scripts\python.exe
set MAIN_SCRIPT=main.py

:: Check if virtual environment exists
if not exist "%PYTHON_EXE%" (
    echo Error: Python virtual environment not found at %PYTHON_EXE%
    echo Please create a virtual environment first with: python -m venv venv
    pause
    exit /b 1
)

:: Check if main script exists
if not exist "%MAIN_SCRIPT%" (
    echo Error: Main script not found at %PROJECT_DIR%%MAIN_SCRIPT%
    pause
    exit /b 1
)

:: Run the Python script
echo Running content monitor...
"%PYTHON_EXE%" "%MAIN_SCRIPT%"

:: Optional: Keep window open to see results (remove for Task Scheduler)
:: pause