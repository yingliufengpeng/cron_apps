from datetime import datetime
from random import randint
from turtle import done

from huggingface_hub import HfApi, hf_hub_download
from plombery import task
from plombery.logger import get_logger


@task
async def download_and_delete_mp4():
    from download_api import hugging_face_hub_download

    _logger = get_logger()

    """Fetch latest 50 sales of the day"""

    _logger.info(f"Running download_and_delete_mp4 at {datetime.now()}")

    await hugging_face_hub_download.download_and_delete_mp4(_logger)
