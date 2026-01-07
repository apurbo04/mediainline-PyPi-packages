from IPython.display import Audio, display
import urllib.request
from mediainline.custom_exception import InvalidURLException
from mediainline.logger import logger


def is_valid_audio_url(url: str) -> bool:
    try:
        response = urllib.request.urlopen(url)
        content_type = response.headers.get("Content-Type", "")

        logger.debug(f"Content-Type: {content_type}")

        return response.status == 200 and content_type.startswith("audio/")
    except Exception as e:
        logger.exception(e)
        return False


def play_audio(
    url: str,
    autoplay: bool = False
) -> str:
    """
    Render an audio player in Jupyter Notebook.

    Args:
        url (str): Direct URL to audio file (.mp3, .wav)
        autoplay (bool): Play automatically or not

    Returns:
        str: success message
    """
    try:
        if not is_valid_audio_url(url):
            raise InvalidURLException("Invalid or non-audio URL")

        audio = Audio(url=url, autoplay=autoplay)
        display(audio)

        return "success"

    except Exception:
        logger.exception("Failed to render audio")
        raise
