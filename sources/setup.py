import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "YouDownload",
    version = "0.1",
    description = "Youtube Video/Audio downloader",
    options = {"build_exe": build_exe_options},
    executables = [Executable("youdownload.py", base=base)]
)