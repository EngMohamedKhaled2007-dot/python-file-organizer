File Organizer V1.0
Made by Eng. Mohamed Khaled
-----------------------------------------
About The Project

File Organizer is a simple Python project that helps organize files automatically.

The program checks the file extensions in a folder and moves each file to its corresponding folder.

For example:

.mp4 -> Videos
.pdf -> PDF
.jpg -> Photos
.html -> Web

I made this project for practice while learning Python and working with files and folders.
-----------------------------------------
Technologies Used

• Python
• pathlib
• csv
• Python Modules
• Basic OOP
-----------------------------------------
How It Works

1. The program reads the folder names and file extensions from "path.csv".
2. It creates the required folders if they don't already exist.
3. It checks the files in the current folder.
4. It moves each file to the folder assigned to its extension.
-----------------------------------------
How To Add A New File Type

To add another type of file:

1. Open "path.csv".
2. Add the folder name and file extension in this format:

FolderName,.extension

Example:

Audio,.mp3

Save the file and close it.

The program will automatically create the "Audio" folder and move .mp3 files into it.

Important:
Do not change the format of the file or add spaces between the folder name and the extension.
-----------------------------------------
How To Run

Requirement:

•Python

To launch the program, run:

launcher.bat

You can also run the program using:

python main.py
-----------------------------------------
Project Structure

main.py -> Runs the program
organizer.py -> Contains the organizing logic
path.csv -> Contains folder names and file extensions
launcher.bat -> Launches the program
-----------------------------------------
Note

This project was made for practice while learning Python.

It is a simple project, but it helped me practice working with files,
folders, CSV files, modules, and basic OOP.

More improvements may be added in future versions.
-----------------------------------------
File Organizer V1.0
Made with Python :)