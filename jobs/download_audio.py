import asyncio
from concurrent.futures import ThreadPoolExecutor

from pytubefix import YouTube
from pytubefix.cli import on_progress
from rich.progress import Progress

from utils.logger import Logger

logger = Logger().logger


def __download(url, console, task_id, progress, out_dir_path):
    yt = YouTube(url.strip(), on_progress_callback=on_progress)
    audio = yt.streams.get_audio_only()

    try:
        audio.download(output_path=out_dir_path)
        console.insert("Downloaded: " + audio.title)
    except Exception as e:
        logger.error(f"Failed to download video from {url}. Error: {str(e)}")
        console.insert(f"Failed to download video from {url}. Error: {str(e)}")
    finally:
        progress.update(task_id, advance=1)


async def __download_all(loop, urls, console, out_dir_path):
    with ThreadPoolExecutor() as executor:
        with Progress() as progress:
            task_id = progress.add_task("Downloading...", total=len(urls))
            tasks = [loop.run_in_executor(executor, __download, url, console, task_id, progress, out_dir_path) for url
                     in urls]
            await asyncio.gather(*tasks)
        logger.info("All downloads are finished")
        console.insert("All downloads are finished")


def start_download_audio(console, urls, out_dir_path):
    console.insert("Start downloading...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(__download_all(loop, urls, console, out_dir_path))
