from tkinter import Tk, BOTH, Canvas, ttk
from ttkthemes import ThemedTk

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)





class Window :
    def __init__(self, width, height):
        self.__root = ThemedTk(theme="yaru")
        self.__root.title("Maze Solver")
        frame = ttk.Frame(self.__root, padding=10)
        frame.grid()    
        self.__canvas = Canvas(frame, bg="white", height=height, width=width)
        self.__canvas.grid(column=0, row=0)
        ttk.Button(frame, text="Hello World").grid(column=0, row=1)
        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()


    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False
        
