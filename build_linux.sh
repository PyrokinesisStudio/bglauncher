pyinstaller Configuration.py --onefile --distpath $PWD/dist_linux
pyinstaller Launcher.py --onefile --distpath $PWD/dist_linux

cp Settings.cfg $PWD/dist_linux/Settings.cfg
cp Configuration.glade $PWD/dist_linux/Configuration.glade
cp Splash.png $PWD/dist_linux/other/Splash.png

rm $PWD/Configuration.spec

rm $PWD/Launcher.spec
