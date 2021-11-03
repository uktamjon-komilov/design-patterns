from tool import Tool


class Brush(Tool):
    def mouse_down(self):
        print("Brush tool")

    def mouse_up(self):
        print("Drawed a line")