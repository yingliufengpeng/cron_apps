@echo off

cd /d E:\cron_tasks


E:\apps\miniconda3\python.exe app_cron.py >>logs/cron.log 2>&1
