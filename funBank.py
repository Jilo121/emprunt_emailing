import tkinter as tk
from tkinter import ttk


def titre(frame_t,texte_t,row_t,col_t):
    titre_element = ttk.Label(chr(frame_t),chr(texte_t), width=20)
    titre_element.grid(row=int(row_t),column=int(col_t))