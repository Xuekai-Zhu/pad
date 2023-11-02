def solution():
    """Jonas is a book collector. He has so many books he is converting his third bedroom into a library. This room has 400 square feet of space. He plans to put several bookshelves in the room and each bookshelf takes up 80 square feet of space. If he reserves 160 square feet of space to use for a desk and some walking space, how many shelves can he put in the room?"""
    # Define the size of each bookshelf and the reserved space
    BOOKSHELF_SIZE = 80
    RESERVED_SPACE = 160

    # Define the size of the room and calculate the available space
    room_size = 400
    available_space = room_size - RESERVED_SPACE

    # Calculate the number of bookshelves that can fit in the room
    num_shelves = available_space // BOOKSHELF_SIZE

    result = num_shelves
    return result

print(solution())