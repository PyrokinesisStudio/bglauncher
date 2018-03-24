pyinstaller Configuration.py ^
    --onefile ^
    --icon utils/Configuration.ico ^
    --noconsole ^
    --key=akjjyglc40028922 ^
    --distpath %cd%

pyinstaller Launcher.py ^
    --onefile ^
    --icon utils/Launcher.ico ^
    --noconsole ^
    --key=akjjyglc40028922 ^
    --distpath %cd%

pause