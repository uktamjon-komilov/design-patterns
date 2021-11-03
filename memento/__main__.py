from history import History
from editor import Editor

editor = Editor()
history = History()

editor.content = "a"
history.push(editor.create_state())

editor.content = "b"
history.push(editor.create_state())

editor.content = "c"
history.push(editor.create_state())
editor.content = history.pop().content

print(editor.content)