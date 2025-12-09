import asyncio
import logging
import os
import random
import shutil
from datetime import datetime

from huggingface_hub import HfApi, hf_hub_download
from plombery.logger import get_logger

os.environ["HF_HUB_URL"] = "https://huggingface.co.cn"

repo_id = "deepseek-ai/DeepSeek-V3"
local_dir = f"tmp/{repo_id}"


async def download_and_delete_mp4(_logger):
    """Fetch latest 50 sales of the day"""
    os.makedirs(local_dir, exist_ok=True)

    # 初始化 API
    api = HfApi()

    # 获取仓库中所有文件信息
    files = api.list_repo_files(repo_id=repo_id, repo_type="model")
    _logger.info(f"仓库文件总数：{len(files)}")

    is_first = random.randint(1, 10) % 2 == 0

    start = random.randint(1, 30) - 1

    start, end = (
        (start, start + 15)
        if is_first
        else (len(files) - start - 15, len(files) - start)
    )

    # start, end = 0, 10

    files = files[start:end]

    # 遍历每个文件，边遍历边下载
    for filename in files:
        _logger.info(f"正在下载：{filename}")
        try:
            local_path = hf_hub_download(
                repo_id=repo_id,
                filename=filename,
                cache_dir=local_dir,  # 本地缓存目录
                resume_download=True,  # 支持断点续传
            )
            _logger.info(f"已下载：{filename} -> {local_path}")
        except Exception as e:
            _logger.error(f"下载失败：{filename}，错误：{e}")

    _logger.info("下载完成")
    shutil.rmtree(local_dir)
    _logger.info(f"{local_dir} 已删除")


if __name__ == "__main__":
    _logger = get_logger()

    asyncio.run(download_and_delete_mp4(_logger))
