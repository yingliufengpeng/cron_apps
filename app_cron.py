import logging
import os
from datetime import datetime

import anyio

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)
os.environ.pop("HTTP_PROXY", None)
os.environ.pop("http_proxy", None)
os.environ.pop("HTTPS_PROXY", None)
os.environ.pop("https_proxy", None)
# === 关键：添加 console handler，这样 >> 才能捕获 ===
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
_logger.addHandler(console_handler)

# 写入独立日志文件（不依赖重定向）
# file_handler = logging.FileHandler("logs/cron.log", encoding="utf-8", delay=False)
# file_handler.setFormatter(formatter)
# file_handler.setLevel(logging.INFO)
# _logger.addHandler(file_handler)


async def download_and_delete_mp4():
    from download_api import hugging_face_hub_download

    """Fetch latest 50 sales of the day"""

    _logger.info(f"Running download_and_delete_mp4 at {datetime.now()}")

    await hugging_face_hub_download.download_and_delete_mp4(_logger)


# 循环定时
# =========================
async def loop_cron(seconds: int = 1):
    interval_seconds = 1  # 转为秒
    while True:
        try:
            await download_and_delete_mp4()
        except Exception as e:
            _logger.error(f"Error occurred: {e}")
        finally:
            pass
        await anyio.sleep(interval_seconds)


# =========================
# 启动
# =========================
anyio.run(loop_cron, 4 * 3600)  # 每 4 小时执行一次
