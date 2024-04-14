from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x300")
logo = PhotoImage(file="vinni-pukh-v-png.png")

label = ttk.Label(text="hello friend!",
                                                            font=("Arial",20),
                                                            borderwidth=5,
                                                            background="red",
                                                            foreground="white",
                                                            padding=10,
                                                            border=12)
ttk.Entry().pack(anchor=N,  padx=10, pady=10)
label1 = ttk.Label(image=logo)
label1.pack()
root.mainloop()

