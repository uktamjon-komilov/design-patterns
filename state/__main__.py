from selection import Selection
from brush import Brush
from canvas import Canvas


canvas = Canvas()

canvas.current_tool = Brush()
canvas.mouse_down()
canvas.mouse_up()

canvas.current_tool = Selection()
canvas.mouse_down()
canvas.mouse_up()