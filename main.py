from __future__ import annotations

import contextlib
import os
from pathlib import Path

from moviepy import CompositeVideoClip, TextClip, VideoFileClip
from moviepy.config import FFMPEG_BINARY, FFPLAY_BINARY, check, try_cmd


def main() -> None:
    """Render a side-by-side video of two video clips."""
    clip1 = VideoFileClip("clip1.mp4")
    clip2 = VideoFileClip("clip2.mp4")

    start_time = 10
    end_time = 15
    clip1 = clip1.subclipped(start_time, end_time)
    clip2 = clip2.subclipped(start_time, end_time)

    target_width = 720
    target_height = 1280
    clip1 = clip1.resized(height=target_height // 2)
    clip2 = clip2.resized(height=target_height // 2)

    font_dir = Path(os.environ["WINDIR"]) / "Fonts"
    txt_clip = TextClip(
        font=font_dir / "Conthrax Bold.otf",
        # font=font_dir / "Arial.ttf",
        text="Hello World!",
        font_size=64,
        # size=(target_width // 2, target_height),
        margin=(0, 0, 0, 24),  # try to fix the incorrect auto-determined size
        color="white",
        bg_color="#ffffff80",
        stroke_color="black",
        stroke_width=2,
        text_align="center",
        duration=end_time - start_time,
    )

    video = CompositeVideoClip(
        clips=[
            clip1.with_position("top"),
            clip2.with_position("bottom"),
            txt_clip.with_position("center"),
        ],
        size=(target_width, target_height),
    )

    if _ffplay_available():
        with contextlib.suppress(IOError):
            video.preview(fps=24, audio_fps=11000)
    elif _ffmpeg_available():
        video.write_videofile("result.mp4", preset="ultrafast", threads=4)


def _ffplay_available() -> bool:
    return try_cmd([FFPLAY_BINARY])[0]


def _ffmpeg_available() -> bool:
    return try_cmd([FFMPEG_BINARY])[0]


if __name__ == "__main__":
    check()
    main()
