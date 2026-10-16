import tkinter as tk

root = tk.Tk()
root.title("Тапсырма 4")

# Сурет салу үшін Canvas (кенва) элементін құрамыз
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Тікбұрыш салу (қызыл түсті) -> (x1, y1, x2, y2)
canvas.create_rectangle(30, 50, 150, 120, fill="red")

# Шеңбер/Овал салу (жасыл түсті)
canvas.create_oval(200, 50, 300, 150, fill="green")

# Үшбұрыш салу (көк түсті) -> үш нүктенің координаталары
canvas.create_polygon(100, 200, 50, 280, 150, 280, fill="blue")

root.mainloop()
