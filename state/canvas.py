class Canvas:
    def __init__(self):
        self._current_tool = None


    def mouse_up(self):
        self._current_tool.mouse_up()
    

    def mouse_down(self):
        self._current_tool.mouse_down()
    

    @property
    def current_tool(self):
        return self._current_tool
    

    @current_tool.setter
    def current_tool(self, tool):
        self._current_tool = tool