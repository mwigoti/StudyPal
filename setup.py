from cx_Freeze import setup, Executable

setup(
    name="studybud",
    version="0.1",
    description="StudyBud",
    executables=[Executable("manage.py")],
    options={
        'build_exe': {
            'packages': [
                'django', 'base', 'rest_framework', 'corsheaders',
                # Include other necessary packages
            ],
        },
    },
)
