Index

Basic information - ln. 8
Tiles - ln. 19
Ending - ln. 53

------------------------------------------------------------------------------
Part 1. Basic information

This version of GEOTEC is still under development and support, so if you have a feature request, send it and I will try to implement it. Some ideas for things to do in this version are:

- create a platformer
- create an rpg
- create a shoot em up

For most of these you will have to modify the engine source itself since I don't have a working pseudo-api working, though I have one in development.

------------------------------------------------------------------------------
Part 2. Tiles

Tiles are a very important part of this engine. To add them, you need to create a savefile, through the Launcher. Currently there are three types of tiles. Normal tiles, sometimes called Geometery, stored in "modularity.json", portals stored in "portals.json", and text, stored in "text.json".

If you want to create a normal tile, you need to do the following:

1. create a new json class
2. create two arrays titled "x" and one called "y"
3. create two integers called "w" and "h" and fill them with what you want the    width and height of your tile to be
4. create an array that is called "tags", all keys before this point have to      have data the next ones can be null
5. create an array called "color" and if not null, fill with three numbers to    represent rgb values.
6. create a string called "texture" and if not null, put the path to the    texture you want to use in the string.
7. create a boolean called "collision"

If you have done all these steps properly, you should have a new tile  ready to be used

If you want to create a new portal, you need to:

1. create a new json class
2. create four arrays called "x1", "y1", "x2", "y2"
3. create two integers called "w" and "h" and fill them with what you want the    width and height of your tile to be
4. create an array called "tags", all keys from this point on can be null, but    this key and before must have data
5. create an array called "color" and if not null, fill with three numbers to     represent rgb values.
6. create a string called texture and if not null, put the path to the texture    you want to use in the string.

If you want to create a new text, you probably should:

1. create a string, you can have anything you want in there
2. create three arrays, those being, "x", "y", and "tags"
3. create a boolean called "isgui"
4. create an array called "bkground_color", that if filled with rgb values
4. create another boolean called "clickable"

------------------------------------------------------------------------------
Part 3. Ending

I hope you enjoy this strange thing, and do many great things with it, have a wonderful day

	- Lemmingsishard of UPGSOFTWARE, part of WIZARDSTUDIOS - 29.6.24

