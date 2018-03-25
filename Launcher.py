import pathlib2
import subprocess
import os
from pprint import pprint, pformat
from ast import literal_eval as litev

Config = {}
sizes_window = ( (640, 480), (800, 600), (1024, 768), (1280, 720), (1366, 768), (1920, 1080) )
sizes_fullscreen = ( (0, 0), (640, 480), (800, 600), (1024, 768), (1280, 720), (1366, 768), (1920, 1080) )
stereo_modes = ( "nostereo", "anaglyph", "sidebyside", "syncdoubling", "3dtvtopbottom", "interlace", "vinterlace", "hwpageflip" )
bit_depths = ( 16, 24, 32 )
refresh_rates = ( 30, 45, 60, 75, 90, 120 )

try:
	with open('Settings.cfg', 'r') as openedfile:
		
		Config = litev( openedfile.read() )
		pprint( 'Settings loaded from ' + openedfile.name )
		
except:
	pprint( 'Couldnt open Settings.cfg, using defaults' )
	Config = { 'videomode' : 0, 'stereomode' : 0, 'nomipmap' : 0, 'fixedtime' : 0, 'sizewindow' : 2, 'sizefullscreen' : 0, 'bitdepth' : 2, 'refreshrate' : 2, 'pathplayer' : 'engine/blenderplayer.exe', 'pathfile' : 'data/main.blend' }
	
if True:
		
	cur_dir = os.path.basename(pathlib2.Path('').resolve().as_posix())
	
	if cur_dir == 'bglauncher':
		
		if os.name == 'nt':
			Config['pathplayer'] = 'dist_win/engine/blenderplayer.exe'
			Config['pathfile'] = 'dist_win/data/testfile.blend'
		
		if os.name == 'posix':
			Config['pathplayer'] = 'dist_linux/engine/blenderplayer'
			Config['pathfile'] = 'dist_linux/data/testfile.blend'
	
	if cur_dir == 'dist_win':
		Config['pathplayer'] = 'engine/blenderplayer.exe'
		Config['pathfile'] = 'data/testfile.blend'
	
	if cur_dir == 'dist_linux':
		Config['pathplayer'] = 'engine/blenderplayer'
		Config['pathfile'] = 'data/testfile.blend'
	
	pathplayer = pathlib2.Path(pathlib2.Path( Config['pathplayer'] ).resolve().as_posix())
	pathfile = pathlib2.Path(pathlib2.Path( Config['pathfile'] ).resolve().as_posix())
	
	command = ''
	
	if pathplayer.exists() and pathfile.exists():
		
		command += '"' + str(pathplayer.as_posix()) + '" '
		
		if Config['videomode'] == 0:
			command += '-w '+ str(sizes_window[Config['sizewindow']][0]) + ' ' + str(sizes_window[Config['sizewindow']][1]) + ' 0 0 '
		
		if Config['videomode'] == 1:
			command += '-f ' + str(sizes_fullscreen[Config['sizefullscreen']][0]) + ' ' + str(sizes_fullscreen[Config['sizefullscreen']][1]) + ' ' + str(bit_depths[Config['bitdepth']]) + ' ' + str(refresh_rates[Config['refreshrate']]) + ' '
			
		command += '-s ' + str(stereo_modes[Config['stereomode']]) + ' '
		
		command += '-g fixedtime=' + str(Config['fixedtime']) + ' '
		
		command += '"' + str(pathfile.as_posix()) + '"'
		
		pprint('Running game under the following command: ')
		pprint(command)
		
		subprocess.Popen(command, shell=True)
