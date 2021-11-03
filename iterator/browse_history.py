from iterator import Iterator

class BrowseHistory:
    def __init__(self):
        self._urls = []
    
    def push(self, url):
        self._urls.append(url)
    
    def pop(self):
        return self._urls.pop()
    
    def create_iterator(self):
        return self.ListIterator(self)
    

    class ListIterator(Iterator):
        def __init__(self, history):
            self._history = history
            self.index = 0

        def has_next(self):
            return (self.index < len(self._history._urls))
        
        def current(self):
            return self._history._urls[self.index]
        
        def next(self):
            self.index += 1