import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Percolation")
    frame = tk.Frame()
    canvas = tk.Canvas(frame, width=1000, height=1000)
    canvas.pack()
    window.mainloop()
