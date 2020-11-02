#My Mouse Cursor Position
#
#Import required modules
import tkinter as tk
from tkinter import messagebox
import platform

running = False     #Monitoring mouse cursor movement is not running

class Program():    #Program functions

    def bttn():     #Function on button press
        global running
        if running == False:    #If the monitor is not running, then start
            running = True
            bttn.config(text='Stop Monitoring')
            Program.start_mon()
        else:                  #If monitor is running, then stop
            running = False
            bttn.config(text='Start Monitoring')
            Program.stop_mon()

    def start_mon():    # Monitor cursor position
        global mon
        x,y = win32api.GetCursorPos()   #Get x and y coordinates of mouse cursor
        cursor_x_pos.config(text=x)     #Write x coordinate of mouse cursor to label
        cursor_y_pos.config(text=y)     #Write y coordinate of mouse cursor to label
        mon = root.after(100,Program.start_mon)  #Loop function every 100 milliseconds

    def stop_mon():
        root.after_cancel(mon)  #Stop program loop
        cursor_x_pos.config(text='')    #Reset labels
        cursor_y_pos.config(text='')

class Window(tk.Frame):         #Window layout
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        global bttn,cursor_x_pos,cursor_y_pos
        self.master = master
        self.master.geometry('310x150')
        self.master.title('Mouse Cursor Tracker')

        cursor_x_lbl = tk.Label(self.master,text='Cursor X Position:')
        cursor_y_lbl = tk.Label(self.master,text='Cursor Y Position:')
        cursor_x_pos = tk.Label(self.master,text='')
        cursor_y_pos = tk.Label(self.master,text='')
        bttn = tk.Button(self.master,text='Start Monitoring',command=Program.bttn)
        cursor_x_lbl.place(x=55,y=20)
        cursor_y_lbl.place(x=55,y=60)
        cursor_x_pos.place(x=200,y=20)
        cursor_y_pos.place(x=200,y=60)
        bttn.place(x=105,y=100)

root = tk.Tk()
if platform.system() != 'Windows':
    root.withdraw()
    messagebox.showerror('Incompatible Operating System','Please run this program on Microsoft Windows')
    exit()
else:
    try:
        import win32api # Module from Pywin32 package
    except:
        root.withdraw()
        messagebox.showerror('Module Not Found','Please install \"Pywin32\" with pip')
        exit()                 #Start Tkinter interpreter and create top window
    app = Window(root)              #Initalize Tkinter window
    root.iconbitmap("cursor.ico")   #Window Titlebar Icon
    root.mainloop()                 #Actual program loop
