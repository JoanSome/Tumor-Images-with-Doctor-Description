# Tumor-Images-with-Doctor-Description

 ## Project Description
 Using python to display tumor images, describe them and save them in a database.

###  Modules
mysql , tkinter, PIL
 
## Long-term Application
An improved efficient application used to view tumor images for evaluation by a doctor. The data (tumor image and description) is saved in a database and can be accessed by other medics.
### Addition functionalities:
1. Once an image has been opened, assessed by a doctor and saved in the database along with the description, the image can be deleted from the directory with the original images. This leaves only images with no description in the folder.

2. A method by which the saved images with descriptions can be displayed. Other medics can then open the images from the database and check the descriptions.


## How to run
Run Main.py
A log in window will pop up, log in.
After logging in, the main window will open. The user can select an image from the 'Tumor Images' folder, write some notes on the text box on the GUI window, then click 'SAVE' button to save the information in a database. The user can click on the 'QUIT' button to close the GUI window or 'NEXT' button to move to the next image.

## Dependencies
mysql Workbench 8.0.33
tkinter 8.6
PIL 9.5.0

