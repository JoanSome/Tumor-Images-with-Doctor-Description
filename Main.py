import mysql.connector
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog

# Connect to the database
my_db = mysql.connector.connect(
    host="localhost",
    user="jsome",
    password="Chemutai96!_",
    database = "tImages"
)
my_cursor = my_db.cursor()

# Create a table called images in the database
my_cursor.execute("CREATE TABLE IF NOT EXISTS images (id INT AUTO_INCREMENT PRIMARY KEY, image LONGBLOB, text VARCHAR(255))")

# Define a function to select images from a directory
def select_image():
    global file_path
    file_path = filedialog.askopenfilename(title="open an Image", filetype=(('image files','*.jpg'),('all files','*.*')))
    img = Image.open(file_path)
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(30,20, anchor = tk.NW, image = photo)
    canvas.image = photo 

# Define a function to save the image and text to the database
def save_image():
    image = Image.open(file_path).tobytes()
    text = text_box.get("1.0", tk.END)
    my_cursor.execute("INSERT INTO images (image, text) VALUES (%s, %s)", (image, text))
    my_db.commit()

def do_something():
    tkMessageBox.showinfo('Status','Image with the notes saved in the database 👌')
    select_button.destroy()
    canvas.destroy()
    describe_label.destroy()
    text_box.destroy()
    save_button.destroy()

# dictionary containing valid usernames and passwords
user_dict = {"Doctor1": "password1", "Doctor2": "password2", "Doctor3": "password3"}

# create a function for login verification
def verify_login():
    username = username_entry.get()
    password = password_entry.get()
    if username in user_dict and password == user_dict[username]:
        login_win.destroy()
    else:
        error_label.config(text="Incorrect username or password")       

# create a function to create the login window
def create_login_window():
    global login_win, username_entry,password_entry, error_label
    login_win = Tk()
    login_win.title("USER LOGIN")
    login_win.geometry("800x800")
    login_win.resizable(False, False)
    login_label = Label(login_win, text = "PLEASE LOGIN", font = "Bold 12")
    username_label = Label(login_win, text="Username:")
    username_entry = Entry(login_win)
    password_label = Label(login_win, text="Password:")
    password_entry = Entry(login_win, show="*")
    error_label = Label(login_win, fg="red")
    login_button = Button(login_win, text="LOGIN",  command=verify_login)

    # arrange the widgets using place method
    login_label.place(x = 320, y = 230)
    username_label.place(x = 300, y = 300)
    username_entry.place(x = 370, y = 300)
    password_label.place(x = 300, y = 350)
    password_entry.place(x = 370, y = 350)
    login_button.place(x = 350, y = 390)
    error_label.place(x = 330, y = 420)

    login_win.mainloop()
create_login_window()

# create a next function which allows one to select a new image and do the whole process again
def next_image():
    create_main_window()

# create a function to create the main window
def create_main_window():
    global main_win, canvas, text_box, select_button, save_button, describe_label
    main_win = Tk()
    main_win.title("Assess Tumor Images...")
    main_win.geometry("800x900")
    main_win.config(bg = '#87ceeb')
    main_win.resizable(False, False)

    # Create two frames, top and bottom
    top_frame = Frame(main_win, bg = '#87ceeb')
    bottom_frame = Frame(main_win, bg = 'skyblue')

    # Create label widgets for the top frames
    select_button = Button(top_frame, text = "SELECT IMAGE", command = select_image)
    select_button.pack(pady = 10)
    canvas = Canvas(top_frame, width = 350, height = 350)
    canvas.pack(pady = 20)
    describe_label = Label(top_frame, text = "Please Enter Tumor Description Below")
    describe_label.pack(pady = 20)
    text_box = Text(top_frame, width = 70, height = 6)
    text_box.pack()
    save_button = Button(bottom_frame, text = "SAVE DATA", command = lambda:[save_image(), do_something()])  
    next_button = Button(bottom_frame, text = 'NEXT', command = next_image)
    next_button.pack(pady = 20)
    quit_button = Button(bottom_frame, text = "QUIT", command = main_win.quit)
    quit_button.pack(pady = 20)
    # pack the frames
    top_frame.pack()
    bottom_frame.pack(pady = 10)

# Run the tkinter event loop
    main_win.mainloop()

create_main_window()