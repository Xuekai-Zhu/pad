def solution():
    """Jonas is converting his third bedroom into a library. This room has 400 square feet of space. He plans to put several bookshelves in the room and each bookshelf takes up 80 square feet of space. If he reserves 160 square feet of space to use for a desk and some walking space, how many shelves can he put in the room?"""
    room_size = 400
    reserved_space = 160
    shelf_size = 80
    max_shelves = (room_size - reserved_space) // shelf_size
    result = max_shelves
    return result

print(solution())