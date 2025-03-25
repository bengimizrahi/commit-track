import datetime
import tkinter as tk
from tkinter import ttk

class SheetView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__setupWindow__()
        self.__setupMain__()
        self.__setupCornerHeading__()
        self.__setupTopHeading__()
        self.__setupStyle__()
    
    def __setupWindow__(self):
        self.title("Commit Tracker")
        self.geometry("200x150")
    
    def __setupMain__(self):
        main = ttk.Frame(self)
        main.pack(expand=True, fill="both")
        main.configure(style="MainFrame.TFrame")
        self.main = main

    def __setupCornerHeading__(self):
        cornerHeading = ttk.Frame(self.main)
        cornerHeading.grid(row=0, column=0, sticky="nsew")
        cornerHeading.configure(style="CornerHeading.TFrame")
        self.cornerHeading = cornerHeading
        
        for i, t in enumerate(["Month", "Day", "Week", "Sprint"]):
            label = ttk.Label(cornerHeading, text=t)
            label.grid(row=i, column=0, sticky="nsew")
            label.configure(anchor="e")
            label.configure(borderwidth=5, relief="sunken")

    def __setupTopHeading__(self):
        topHeading = ttk.Frame(self.main)
        topHeading.grid(row=0, column=1, sticky="nsew")
        topHeading.configure(style="TopHeading.TFrame")
        self.topHeading = topHeading

        numDays = 40
        firstDate = datetime.date.today()
        for i in range(numDays):
            date = firstDate + datetime.timedelta(days=i)
            label = ttk.Label(topHeading, text=str(date.month), width=1)
            label.grid(row=0, column=i, sticky="nsew")
            label.configure(anchor="center")
            label.configure(borderwidth=5, relief="sunken")
            label = ttk.Label(topHeading, text=str(date.day))
            label.grid(row=1, column=i, sticky="nsew")
            label.configure(anchor="center")
            label.configure(borderwidth=5, relief="sunken")
            week = date.isocalendar()[1]
            sprint = week//2 + 1
            label = ttk.Label(topHeading, text=str(week))
            label.grid(row=3, column=i, sticky="nsew")
            label.configure(anchor="center")
            label.configure(borderwidth=5, relief="sunken")
            label = ttk.Label(topHeading, text=str(sprint))
            label.grid(row=2, column=i, sticky="nsew")
            label.configure(anchor="center")
            label.configure(borderwidth=5, relief="sunken")

    def __setupStyle__(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("MainFrame.TFrame", background="lightblue")
        style.configure("CornerHeading.TFrame", background="lightgreen")
        style.configure("TopHeading.TFrame", background="lightyellow")
        self.style = style
    
if __name__ == "__main__":
    sheetView = SheetView()
    sheetView.mainloop()