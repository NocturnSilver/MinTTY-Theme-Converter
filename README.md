# MinTTY-Theme-Converter

## Overview
    
    Creates a theme for git bash on Windows given 19 colors. 
    The program takes in a filename as input and produces a file
    that is to be placed in "C:/Program Files/Git/usr/share/mintty/themes"
    The program uses the  16-Color ANSI Palette (used by CLI tools) + 3 colors 
    for ForegroundColour, BackgroundColour, CursorColour
    
## Usage
  
python gitThemeMaker.py [filename] [option]
    
Options:
    
-h / --help                               prints the help on the terminal
-d / --default                            attempts to save the file in "C:/Program Files/Git/usr/share/mintty/themes"
-o [path/filename] / -O [path/filename]   saves the result on the specified path on the filename
    
---------------------------------------------------------------------------------------------------------------
    
    file Format as input:
    
    Hexcolor1 # ForegroundColour
    Hexcolor2 # BackgroundColour
    Hexcolor3 # CursorColour
       .
       .
       .
    Hexcolor17 # BoldMagenta	
    Hexcolor18 # BoldCyan	
    Hexcolor19 # BoldWhite
    
    The order of how the colors are arranged are shown below
    
    ---------------------------------------------------------------------------------------------------------------
    
    Uses the 16-Color ANSI Palette (used by CLI tools)
    - 8 bright colors
    - 8 (bold colors)

    ForegroundColour   x	Default text color. Anything printed without ANSI color codes.
    BackgroundColour   x	Default background color.
    CursorColour       x    The block of bar cursor color

    Black              0	Often used as a background by some apps; rarely used as text.
    Red	               1	Errors, warnings, deletion (e.g., git diff deleted lines).
    Green              2	Success output, additions (git diff added lines).
    Yellow             3	Warnings, special notices.
    Blue               4	Directory names in ls, some UI accents.
    Magenta            5	Less common; used for prompts or highlights in some themes.
    Cyan               6	Symlinks in ls, informational messages.
    White              7	Default light text for many tools (less common when ForegroundColour is set).

    BoldRed            9	High-intensity errors or important alerts.
    BoldGreen	       10	High-visibility success messages.
    BoldYellow	       11	Emphasized warnings.
    BoldBlue	       12	Highlighted directories, UI accents.
    BoldMagenta	       13	Rare but used for prompts/themes.
    BoldCyan	       14	Highlighted informational messages.
    BoldWhite	       15	Brightest text; often used for prompt or emphasized output.
    
    ---------------------------------------------------------------------------------------------------------------
    
    Future updates:
    - Allow different file types to be accepted: csv, json, ...
    - Allow RGB values to be used in the file instead of Hex converted to RGB
    - Check the output file if it follows the standard that is accepted
    - accept key-value pairs in the file
