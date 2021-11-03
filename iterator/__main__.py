from browse_history import BrowseHistory

history = BrowseHistory()

history.push("https://youtube.com")
history.push("https://google.com")
history.push("https://instagram.com")

iterator = history.create_iterator()

while iterator.has_next():
    element = iterator.current()

    # Do something with the current element
    # print(element)

    iterator.next()