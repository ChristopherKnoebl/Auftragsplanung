import tkinter
import sqlite3
from tkinter import ttk

main = tkinter.Tk()

buFenster = ttk.Button(main, text="Auftrag erstellen")
buFenster.grid(row=0, column=0, padx=5, pady=5)

buFenster = ttk.Button(main, text="Tabelle abfragen")
buFenster.grid(row=0, column=1, padx=5, pady=5)

tkinter.mainloop()
