pyinstaller Configuration.py --onefile --icon Configuration.ico --noconsole --distpath %cd%/dist_win

pyinstaller Launcher.py --onefile --icon Launcher.ico --noconsole --distpath %cd%/dist_win

copy /Y "Settings.cfg" "%cd%/dist_win/Settings.cfg"
copy /Y "Configuration.glade" "%cd%/dist_win/Configuration.glade"
copy /Y "Splash.png" "%cd%/dist_win/other/Splash.png"

del "Configuration.spec"
del "Launcher.spec"

pause