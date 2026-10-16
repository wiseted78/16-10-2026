import tkinter as tk
from tkinter import ttk # ttk ішінде Combobox (таңдау мәзірі) бар

def change_color(event):
    # Мәзірден таңдалған түсті алып, терезенің фонына орнатамыз
    selected_color = color_menu.get()
    
    # Тілдерді сәйкестендіру (Қазақша атауды жүйелік түске көшіру)
    color_map = {"Ақ": "white", "Сары": "yellow", "Сұр": "gray", "Қызыл": "red"}
    
    root.config(bg=color_map[selected_color])

root = tk.Tk()
root.title("Тапсырма 5")
root.geometry("400x300")

# Таңдау мәзірін (Combobox) құру
color_menu = ttk.Combobox(root, values=["Ақ", "Сары", "Сұр", "Қызыл"])
color_menu.pack(pady=20)
color_menu.current(0) # Әдепкі бойынша бірінші элемент тұрады

# Мәзірден бірдеңе таңдалғанда функцияны шақыру (Bind)
color_menu.bind("<<ComboboxSelected>>", change_color)

root.mainloop()
