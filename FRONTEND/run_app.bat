@echo off
echo Starting SMS Spam Classifier App...
echo.
cd /d "%~dp0"
streamlit run app.py
pause
