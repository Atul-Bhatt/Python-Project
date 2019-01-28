import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


class SeaOfBTCApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="finance.ico")
        tk.Tk.wm_title(self, "Bitcoin Trading App")

        container = tk.Frame()
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # create a dictionary of frames
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button = ttk.Button(self, text="page one", command=lambda: controller.show_frame(PageOne))
        button.pack()
        button1 = ttk.Button(self, text="page two", command=lambda: controller.show_frame(PageTwo))
        button1.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One !!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button = ttk.Button(self, text="start page", command=lambda: controller.show_frame(StartPage))
        button.pack()
        button1 = ttk.Button(self, text="page two", command=lambda: controller.show_frame(PageTwo))
        button1.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two !!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button = ttk.Button(self, text="start page", command=lambda: controller.show_frame(StartPage))
        button.pack()
        button1 = ttk.Button(self, text="page one", command=lambda: controller.show_frame(PageOne))
        button1.pack()


app = SeaOfBTCApp()
app.mainloop()
