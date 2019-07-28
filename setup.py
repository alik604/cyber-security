from cx_Freeze import setup, Executable

setup(
    name='Eyecare',
    version='1.0',
    url='',
    license='',
    author='alik604',
    author_email='',
    options={'build_exe': {'include_files': ['autorun.inf']}},
    executables=[Executable("myMalware.py", base=None)],
    description='please note this is not safe software '
)
