from tool import Tool


class Selection(Tool):
    def mouse_down(self):
        print("Selection icon")
    
    def mouse_up(self):
        print("Selected an item")