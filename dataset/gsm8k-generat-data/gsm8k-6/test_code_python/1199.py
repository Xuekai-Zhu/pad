def solution():
    # Calculate the available space for bookshelves
    available_space = 400 - 160  # reserve 160 square feet for desk and walking space
    shelf_space = 80  # each bookshelf takes up 80 square feet of space

    # Calculate the number of bookshelves that can fit in the room
    num_shelves = available_space // shelf_space
    result = num_shelves
    return result

print(solution())