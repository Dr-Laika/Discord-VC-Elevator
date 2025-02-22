call .venv\Scripts\activate %*
python.exe -m pip install --upgrade pip %*
python vc_elevator.py %*
deactivate
pause