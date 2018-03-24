# BGLauncher
Blender Game Engine tool to aid game configuration and launching.

The goal of this simple tool is:
- To easily start a game in BGE using a previously saved configuration;
- To easily configure the settings before starting the game;
- Allow the developer to change the executable icon (not possible on blenderplayer.exe);

The use of BGLauncher is simple, yet powerful. The tool consists in two executables, the Configuration and Launcher.
- The Configuration opens a configuration window, where the user can set the settings and start the game from it.
- The Launcher opens the game without any window or dialog, using the saved settings.
- The file Settings.cfg stores the settings that can be changed by the user when using Configuration executable, and also contains some needed paths to run the game (blenderplayer and main game file relative paths, actually).
