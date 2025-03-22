import tkinter as tk

import tkinter as tk
from tkinter import ttk


class SheetView(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.rowconfigure(0, weight=10)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=0)

        leftCanvas = tk.Canvas(self)
        leftCanvas.grid(row=0, column=0, sticky="nsew")
        rightCanvas = tk.Canvas(self)
        rightCanvas.grid(row=0, column=1, sticky="nsew")
        def vscrollCmd(*args):
            leftCanvas.yview(*args)
            rightCanvas.yview(*args)
        
        self.leftInnerFrame = ttk.Frame(leftCanvas)
        self.leftInnerFrame.bind("<Configure>",
                lambda e: leftCanvas.configure(scrollregion=leftCanvas.bbox("all")))
        leftCanvas.create_window((0, 0), window=self.leftInnerFrame, anchor="nw")

        self.rightInnerFrame = ttk.Frame(rightCanvas)
        self.rightInnerFrame.bind("<Configure>",
                lambda e: rightCanvas.configure(scrollregion=rightCanvas.bbox("all")))
        rightCanvas.create_window((0, 0), window=self.rightInnerFrame, anchor="nw")

        verticalScrollbar = ttk.Scrollbar(self, orient="vertical", command=vscrollCmd)
        leftCanvas.configure(yscrollcommand=verticalScrollbar.set)
        rightCanvas.configure(yscrollcommand=verticalScrollbar.set)
        verticalScrollbar.grid(row=0, column=2, sticky="nsew")

        horizontalScrollbar = ttk.Scrollbar(self, orient="horizontal", command=rightCanvas.xview)
        horizontalScrollbar.grid(row=1, column=1, sticky="nsew")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scrollable Frame Example")

    sheetView = SheetView(root)
    sheetView.pack(fill="both", expand=True)

    # Add many widgets inside the scrollable frame
    for i in range(50):
        tk.Button(sheetView.leftInnerFrame, text=f"Bengi Mizrahi").grid(row=i, column=0, sticky="e")
        tk.Button(sheetView.rightInnerFrame, text=f"Label {i}").pack()

    root.mainloop()