@echo off
echo ========================================
echo Starting Pinterest Affiliate Website
echo ========================================
echo.

cd /d "%~dp0"

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo.
echo Installing/updating requirements...
pip install -r requirements.txt

echo.
echo ========================================
echo Starting Flask server...
echo ========================================
echo.
echo Your website will be available at:
echo http://localhost:5000
echo.
echo Press CTRL+C to stop the server
echo ========================================
echo.

python app.py

pause
