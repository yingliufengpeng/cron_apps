import logging
import os
import sys

# 删除系统中设置的 HTTP/HTTPS 代理环境变量
os.environ.pop("HTTP_PROXY", None)
os.environ.pop("http_proxy", None)
os.environ.pop("HTTPS_PROXY", None)
os.environ.pop("https_proxy", None)


from apscheduler.triggers.interval import IntervalTrigger
from plombery import Trigger, register_pipeline

from jobs.task import download_and_delete_mp4

# ------------------------
# 确保日志目录存在
# ------------------------
os.makedirs("logs", exist_ok=True)

# ------------------------
# 配置全局日志
# ------------------------
logger = logging.getLogger("plombery")
logger.setLevel(logging.INFO)

# file_handler = logging.FileHandler("logs/plombery.log", encoding="utf-8")
# file_handler.setLevel(logging.INFO)
# formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# ------------------------
# 注册 pipeline + triggers
# ------------------------
register_pipeline(
    id="download_pipeline",
    description="Download mp4",
    tasks=[download_and_delete_mp4],
    triggers=[
        Trigger(
            id="every_4_hours",
            name="Every 4 Hours",
            description="Run the pipeline every 4 hours",
            schedule=IntervalTrigger(hours=4),  # 修改这里
        ),
    ],
)

# ------------------------
# 启动 Web UI
# ------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("plombery:get_app", reload=False, factory=True)
