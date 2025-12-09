@echo off

cd /d E:\cron_tasks


E:\apps\miniconda3\pythonw.exe app.py >>logs/plombery.log 2>&1
