# pip install cx_Freeze
from cx_Freeze import setup, Executable

# Define the options for cx_Freeze
build_exe_options = {
    "packages": [],  # List of packages to include, if any
    "excludes": [],  # List of modules to exclude, if any
}

# Setup configuration
setup(
    name="FlappyBox",
    version="0.1",
    description="Flappy Box Game",
    options={"build_exe": build_exe_options},
    executables=[Executable("Main.py", base="Win32GUI", target_name="FlappyBox.exe")] # for CrossPlatform base none targetname .exe .app none 
)
# python setup.py build Run on cmd
