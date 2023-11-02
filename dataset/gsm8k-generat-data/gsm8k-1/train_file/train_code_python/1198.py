def solution():
    """Jonas is a book collector. He has so many books he is converting his third bedroom into a library. This room has 400 square feet of space. He plans to put several bookshelves in the room and each bookshelf takes up 80 square feet of space. If he reserves 160 square feet of space to use for a desk and some walking space, how many shelves can he put in the room?"""
    room_space = 400
    reserved_space = 160
    bookshelf_space = 80
    available_space = room_space - reserved_space
    shelves = available_space // bookshelf_space
    result = shelves
    return result

print(solution())