 
 # 安装
    pip install -r requirements.txt
    
 
# 服务启动  
  python  app.py    (端口默认8000)
  
  或者 
  
  start run_schedule.bat
  
 
# 注册定时任务(windows)  定时任务暂时不用
  SCHTASKS /Create /SC MINUTE /MO 30 /TN "PlomberyScheduler" /TR "E:\cron_apps\run_scheduler.bat" /RL HIGHEST /F
   
   
  SCHTASKS /Create /SC MINUTE /MO 1 /TN "PlomberySchedulerCron" /TR "E:\cron_apps\run_scheduler_cron.bat" /RL HIGHEST /F

# 删除定时任务(windows)
  SCHTASKS /Delete /TN "PlomberyScheduler" /F
  SCHTASKS /Delete /TN "PlomberySchedulerCron" /F


# 创建windows PllmberyService 服务 

  nssm install PlomberyService "C:\Windows\System32\cmd.exe" "/c E:\cron_apps\run_scheduler.bat"
  
  nssm set PlomberyService AppDirectory "E:\cron_apps"
  
  nssm.exe set PlomberyService ObjectName ".\peng" "xxxxxx"

  
# 启动服务/停止服务/重启 PllmberyService服务
  nssm start PlomberyService
  nssm stop PlomberyService
  nssm restart PlomberyService

# 删除windows服务

  nssm.exe remove PlomberyService confirm


# 创建windows DownloadCronService 服务 

  nssm install DownloadCronService "C:\Windows\System32\cmd.exe" "/c E:\cron_apps\run_scheduler_cron.bat"  
  
  nssm set DownloadCronService AppDirectory "E:\cron_apps"
  
  nssm.exe set DownloadCronService ObjectName ".\peng" "xxxxxx"

  
# 启动服务/停止服务/重启 PllmberyService服务
  nssm start DownloadCronService
  nssm stop DownloadCronService
  nssm restart DownloadCronService

# 删除DownloadCronService服务

  nssm.exe remove DownloadCronService confirm
  

# windows服务通过 nssm 来做管理, 权限为管理员权限.

  文件路径: deploy\nssm.exe
