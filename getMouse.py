#My Mouse Cursor Position
#
#Import required modules
import tkinter as tk
from tkinter import messagebox
try:
    import win32api # Module from Pywin32 package
except:
    mod_not_found = messagebox.showerror('Module not installed','Please install \"Pywin32\" with pip.')

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

    def start_mon():   #Start function
        global mon
        x,y = win32api.GetCursorPos()   #Get x and y coordinates of mouse cursor
        cursor_x_pos.config(text=x)
        cursor_y_pos.config(text=y)
        mon = root.after(100,Program.start_mon)  #Start monitoring mouse cursor

    def stop_mon():    #Stop function
        root.after_cancel(mon)  #Stop program loop
        cursor_x_pos.config(text='')    #Reset labels
        cursor_y_pos.config(text='')

class Window(tk.Frame):         #Window layout
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        global bttn,cursor_x_pos,cursor_y_pos
        self.master = master
        self.master.geometry('310x150')
        self.master.title('My Mouse Cursor Position')

        cursor_x_lbl = tk.Label(self.master,text='Cursor X Position:')
        cursor_y_lbl = tk.Label(self.master,text='Cursor Y Position:')
        cursor_x_pos = tk.Label(self.master,text='')
        cursor_y_pos = tk.Label(self.master,text='')
        bttn = tk.Button(self.master,text='Start Monitoring',command=Program.bttn)
        cursor_x_lbl.place(x=30,y=20)
        cursor_y_lbl.place(x=30,y=60)
        cursor_x_pos.place(x=160,y=20)
        cursor_y_pos.place(x=160,y=60)
        bttn.place(x=105,y=100)

root = tk.Tk()                  #Start Tkinter interpreter and create top window
app = Window(root)              #Initalize Tkinter window
root.iconbitmap("cursor.ico")   #Window Titlebar Icon
root.mainloop()                 #Actual program loop
