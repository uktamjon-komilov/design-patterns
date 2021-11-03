class EditorState:
    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        return self._content