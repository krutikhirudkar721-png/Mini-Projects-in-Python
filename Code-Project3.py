import tkinter as tk
from tkinter import ttk
from time import strftime

def update_time():
    current_time = strftime('%I:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
root.configure(bg='#121212')

window_width = 500
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

style = ttk.Style()
style.configure(
    'TLabel', 
    background='#121212', 
    foreground='#FF5F1F', 
    font=('DS-Digital', 75, 'bold')
)

clock_label = ttk.Label(root, style='TLabel', anchor='center')
clock_label.pack(expand=True, fill='both')

update_time()
root.mainloop()
