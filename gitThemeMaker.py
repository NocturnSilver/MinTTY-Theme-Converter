helpstr = """
    
    ---------------------------------------------------------------------------------------------------------------
    
    Creates a theme for git bash on Windows given 19 colors. 
    The program takes in a filename as input and produces a file
    that is to be placed in "C:/Program Files/Git/usr/share/mintty/themes"
    The program uses the  16-Color ANSI Palette (used by CLI tools) + 3 colors 
    for ForegroundColour, BackgroundColour, CursorColour
    
    ---------------------------------------------------------------------------------------------------------------
    
    Usage:
    
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

"""
import sys
from pathlib import Path

# ---------------------------------------------- C O L O R - F U N C T I O N S -----------------------------------------------

def hexToRgb(color):
    """ Turns the Hex color into RGB """
    color = str(color)
    print(color)
    hex = color.lstrip('#')
    tup = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    rgb = str(tup).strip("()").replace(" ","")
    return rgb

def updateColors():
    """ Updates the colors in the dictionary"""
    
    if not checkFile():
        # Create a list of ordered colors
        with open(FILE, "r") as f: colList = f.read().splitlines()
                
        i = 0
        # store the values in the color dictionary
        for key,value in colorDict.copy().items(): 
            colorDict.update({key: hexToRgb(colList[i])})
            i += 1
        
    else:
        raise Exception("File either in wrong format, or not enough colors")

# ---------------------------------------------- S Y S T E M - F U N C T I O N S------------------------------------------------

def pathCheck():
    """ Check if the path exists and return path if valid."""
   
    if not PATH.exists():
        # If path does not exist then set to current working directory
        try:
            PATH.touch(exist_ok=True)
        except:
            print("File does not exist, and cannot create file with chose name. Will name file as output")
            return Path("./output").resolve()
    

def optionParser(option):
    match option:
        # help cases
        case "-h": 
            print(helpstr)
            sys.exit()
        case "--help": 
            print(helpstr)
            sys.exit(0)
            
        # Option to insert directly into the themes
        case "-i": 
            if len(sys.argv) == 3:
                return Path("C:/Program Files/Git/usr/share/mintty/themes").resolve()
            else:
                raise FileNotFoundError("A path was not supplied")
            
        # option to output files in a specified directory
        case "-o": 
            if len(sys.argv) == 4:
                # return a path to the file 
                return Path(sys.argv[3]).resolve()
            else: 
                raise FileNotFoundError("A path was not supplied")
                
        case "-O":
            if len(sys.argv) == 4:
                # return a path to the file
                return Path(sys.argv[3]).resolve()
            else: 
                raise FileNotFoundError("A path was not supplied")
                
        case _:
            if not Path(sys.argv[1]).resolve().exists():
                raise FileNotFoundError(f"File not found {sys.argv[1]}") 
            return Path(sys.argv[1]).resolve()
    

def checkFile():
    """ Check if file has a minimum of 16 lines"""
    with open(FILE, "rb") as f: num_lines = sum(1 for _ in f)
    if num_lines < 16: return 1
    else: return 0

def writeFile():
    """ Write the colors"""
    print(f"PATH = {PATH}")
    with PATH.open("w") as f:
        for key,value in colorDict.items():
            f.write(f"{key}={value}\n")

# ----------------------------------------------------- M A I N --------------------------------------------------------------

def main():

    # update the color dictionary
    updateColors()
    
    # write the RGB colors into a file
    writeFile()
    
    return 0

# expect only the file to be processed
if len(sys.argv) ==  2: 
    FILE = optionParser(sys.argv[1])
elif len(sys.argv) >  2:
    print(sys.argv)
    FILE = Path(sys.argv[1]).resolve()
    PATH = optionParser(sys.argv[2])
    pathCheck()
else:
    print(helpstr)
    sys.exit()
    
print(f"SYSARGV[3] = {sys.argv[3]}")

colorDict = {
    "ForegroundColour": "",
    "BackgroundColour": "",
    "CursorColour": "",
    "Black": "",
    "BoldBlack": "",
    "Red": "",
    "BoldRed": "",
    "Green": "",
    "BoldGreen": "",
    "Yellow": "",
    "BoldYellow": "",
    "Blue": "",
    "BoldBlue": "",
    "Magenta": "",
    "BoldMagenta": "",
    "Cyan": "",
    "BoldCyan": "",
    "White": "",
    "BoldWhite": ""
}

main()
        