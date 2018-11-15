import os
import sys
from pytube import YouTube
from cx_Freeze import setup, Executable

setup(
    name = "PyYT_Downloader by Irnil",
    version = "0.1",
    description = "Lite You Tube dowloader",
    executables = [Executable("YTD_load.py")]
)