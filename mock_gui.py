import tkinter as tk
from tkinter import ttk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Commit Tracker")
        self.geometry("1400x1000")
        self.createWidgets()

    def createWidgets(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("RootFrame.TFrame", background="lightblue")
        style.configure("WorklogFrame.TFrame", background="lightcoral")
        style.configure("TasksFrame.TFrame", background="lightgreen")

        self.rootFrame = ttk.Frame(self, padding=2)
        self.rootFrame.pack(expand=True, fill="both")
        self.rootFrame.rowconfigure(0, weight=1)
        self.rootFrame.rowconfigure(1, weight=1)
        self.rootFrame.columnconfigure(0, weight=1)

        self.worklogFrame = ttk.Frame(self.rootFrame, padding=2)
        self.worklogFrame.grid(row=0, sticky="nsew")
        self.worklogFrame.configure(style="WorklogFrame.TFrame")
        self.worklogScrollbar = ttk.Scrollbar(self.worklogFrame, orient="vertical")
        self.worklogScrollbar.pack(side="right", fill="y")

        # self.worklogText = tk.Text(self.worklogFrame, yscrollcommand=self.worklogScrollbar.set)
        # self.worklogText.pack(expand=True, fill="both")
        # self.worklogScrollbar.config(command=self.worklogText.yview)
        self.tasksFrame = ttk.Frame(self.rootFrame, padding=2)
        self.tasksFrame.grid(row=1, sticky="nsew")
        self.tasksFrame.configure(style="TasksFrame.TFrame")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()