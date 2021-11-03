class History:
    def __init__(self):
        self._history = []
    

    def push(self, state):
        self._history.append(state)
    

    def pop(self):
        self._history.pop()
        return self._history[-1]