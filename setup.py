from cx_Freeze import setup, Executable


files = ['logo.png', 'nume.html']


setup(
    name="NumeIDE",
    version="0.1",
    description="Code editor",
    executables=[Executable("nume.py")],
    options={
        'build_exe': {
            'include_files': files
        }
    }
)
