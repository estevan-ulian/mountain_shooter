from cx_Freeze import setup, Executable
import os

asset_path = './asset'
asset_list = os.listdir(asset_path)
asset_list_complete = [os.path.join('asset', asset).replace("\\", "/") for asset in asset_list
                       ]
print(asset_list_complete)

executables = [Executable('main.py')]
files = {"include_files": asset_list_complete, "packages": ["pygame"]}

setup(
    name="MountainShooter",
    version="1.0",
    description="A simple 2D shooting game",
    options={"build_exe": {"packages": ["pygame"], }},
    executables=executables,
)
