import gtk
import pathlib2
import os
import gobject
import subprocess
from pprint import pprint, pformat
from ast import literal_eval

Config = None
sizes_window = ( (640, 480), (800, 600), (1024, 768), (1280, 720), (1366, 768), (1920, 1080) )
sizes_fullscreen = ( (0, 0), (640, 480), (800, 600), (1024, 768), (1280, 720), (1366, 768), (1920, 1080) )
stereo_modes = ( "nostereo", "anaglyph", "sidebyside", "syncdoubling", "3dtvtopbottom", "interlace", "vinterlace", "hwpageflip" )
bit_depths = ( 16, 24, 32 )
refresh_rates = ( 30, 45, 60, 75, 90, 120 )

try:
	path = pathlib2.Path( 'Settings.cfg' ).resolve()
	
	with open(path.as_posix(), 'r') as openedfile:
		Config = literal_eval( openedfile.read() )
	
except:
	pprint('Could not open Settings.cfg')

#pprint(Config)
	
def on_ButtonPlay_clicked(event):
	
	cur_dir = os.path.basename(os.path.dirname(__file__))
	
	if cur_dir == 'bglauncher':
		
		if os.name == 'nt':
			Config['pathplayer'] = 'dist_win/engine/blenderplayer.exe'
			Config['pathfile'] = 'dist_win/data/testfile.blend'
			Config['pathsplash'] = 'dist_win/other/Splash.png'
		
		if os.name == 'posix':
			Config['pathplayer'] = 'dist_linux/engine/blenderplayer.exe'
			Config['pathfile'] = 'dist_linux/data/testfile.blend'
			Config['pathsplash'] = 'dist_linux/other/Splash.png'
	
	if cur_dir == 'dist_win':
		Config['pathplayer'] = 'engine/blenderplayer.exe'
		Config['pathfile'] = 'data/testfile.blend'
		Config['pathsplash'] = 'data/other/Splash.png'
	
	if cur_dir == 'dist_linux':
		Config['pathplayer'] = 'engine/blenderplayer'
		Config['pathfile'] = 'data/testfile.blend'
		Config['pathsplash'] = 'data/other/Splash.png'
	
	pathplayer = pathlib2.Path( Config['pathplayer'] ).resolve()
	pathfile = pathlib2.Path( Config['pathfile'] ).resolve()
	
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
		
	splash = builder.get_object('WindowSplash')
	image = builder.get_object('ImageSplash')
	main = builder.get_object('MainWindow')
	image.set_from_file(Config['pathsplash'])
	splash.show()
	main.hide_all()
	gobject.timeout_add(Config['splashtime'], on_timeout)

def on_timeout():
	gtk.main_quit()
	
def on_ButtonSave_clicked(event):
		
	try:
		with open('Settings.cfg', 'w') as openedfile:
			
			openedfile.write( pformat( Config ) )
			pprint( 'Settings saved to ' + openedfile.name )
			
	except:
		pprint( 'Couldnt save settings to Settings.cfg' )

def on_ComboRefreshRate_changed(event):
	Config['refreshrate'] = int(event.get_active())
	pprint('Refresh rate set to ' + str(Config['refreshrate']))

def on_ComboBitDepth_changed(event):
	Config['bitdepth'] = int(event.get_active())
	pprint('Bit depth set to ' + str(Config['bitdepth']))

def on_ComboFullscreenResolution_changed(event):
	Config['sizefullscreen'] = int(event.get_active())
	pprint('Fullscreen resolution set to ' + str(Config['sizefullscreen']))

def on_ComboWindowSize_changed(event):
	Config['sizewindow'] = int(event.get_active())
	pprint('Window size set to ' + str(Config['sizewindow']))

def on_ComboVideoMode_changed(event):
	Config['videomode'] = int(event.get_active())
	pprint('Video mode set to ' + str(Config['videomode']))

def on_ComboStereoMode_changed(event):
	Config['stereomode'] = int(event.get_active())
	pprint('Stereo mode set to ' + str(Config['stereomode']))

def on_CheckFixedTime_toggled(event):
	Config['fixedtime'] = int(event.get_active())
	pprint('Fixed time set to ' + str(Config['fixedtime']))

def on_CheckNoMipmap_toggled(event):
	Config['nomipmap'] = int(event.get_active())
	pprint('Disable mipmaps set to ' + str(Config['nomipmap']))

handlers = {
'on_ButtonQuit_clicked' : gtk.main_quit,
'on_ButtonPlay_clicked' : on_ButtonPlay_clicked,
'on_ButtonSave_clicked' : on_ButtonSave_clicked,
'on_ComboRefreshRate_changed' : on_ComboRefreshRate_changed,
'on_ComboFullscreenResolution_changed' : on_ComboFullscreenResolution_changed,
'on_ComboWindowSize_changed' : on_ComboWindowSize_changed,
'on_ComboVideoMode_changed' : on_ComboVideoMode_changed,
'on_ComboStereoMode_changed' : on_ComboStereoMode_changed,
'on_ComboBitDepth_changed' : on_ComboBitDepth_changed,
'on_CheckFixedTime_toggled' : on_CheckFixedTime_toggled,
'on_CheckNoMipmap_toggled' : on_CheckNoMipmap_toggled
}

# Builder
builder = gtk.Builder()
builder.add_from_file("Configuration.glade")
builder.connect_signals(handlers)

# Show all
window = builder.get_object("MainWindow")
window.show_all()
builder.get_object("ComboStereoMode").set_active(Config['stereomode'])
builder.get_object("ComboVideoMode").set_active(Config['videomode'])
builder.get_object("ComboWindowSize").set_active(Config['sizewindow'])
builder.get_object("ComboFullscreenResolution").set_active(Config['sizefullscreen'])
builder.get_object("ComboBitDepth").set_active(Config['bitdepth'])
builder.get_object("ComboRefreshRate").set_active(Config['refreshrate'])

# Initialize
gtk.main()