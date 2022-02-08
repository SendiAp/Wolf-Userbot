import os
from typing import Optional

from moviepy.editor import VideoFileClip
from PIL import Image

from ...core.logger import logging
from ...core.managers import edit_or_reply
from ..tools import media_type
from .utils import runcmd

LOGS = logging.getLogger(__name__)


async def media_to_pic(event, reply, noedits=False):  # sourcery no-metrics
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    if not noedits:
        wolfevent = await edit_or_reply(
            event, f"`Transfiguration Time! Converting to ....`"
        )
    else:
        wolfevent = event
    wolfmedia = None
    wolffile = os.path.join("./temp/", "meme.png")
    if os.path.exists(drgfile):
        os.remove(drgfile)
    if mediatype == "Photo":
        wolfmedia = await reply.download_media(file="./temp")
        im = Image.open(wolfmedia)
        im.save(wolffile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, drgfile, thumb=-1)
    elif mediatype == "Sticker":
        wolfmedia = await reply.download_media(file="./temp")
        if wolfmedia.endswith(".tgs"):
            wolfcmd = f"lottie_convert.py --frame 0 -if lottie -of png '{drgmedia}' '{drgfile}'"
            stdout, stderr = (await runcmd(drgcmd))[:2]
            if stderr:
                LOGS.info(stdout + stderr)
        elif drgmedia.endswith(".webp"):
            im = Image.open(wolfmedia)
            im.save(drgfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, drgfile, thumb=-1)
        if not os.path.exists(drgfile):
            drgmedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(catfile, 0.1)
            except:
                clip = clip.save_frame(catfile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            wolfmedia = await reply.download_media(file="./temp")
            im = Image.open(drgmedia)
            im.save(wolffile)
    if catmedia and os.path.lexists(drgmedia):
        os.remove(wolfmedia)
    if os.path.lexists(drgfile):
        return wolfevent, wolffile, mediatype
    return wolfevent, None


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        LOGS.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
