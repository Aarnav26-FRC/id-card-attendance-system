@echo off
echo ========================================================
echo Starting SRU Smart ID Card Attendance Management System
echo ========================================================
pip install flask opencv-python numpy
python seed_data.py
python app.py
pause
