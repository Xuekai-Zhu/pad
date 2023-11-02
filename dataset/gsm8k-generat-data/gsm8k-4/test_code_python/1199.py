def solution():
    """Jonas is a book collector. He has so many books he is converting his third bedroom into a library. This room has 400 square feet of space. He plans to put several bookshelves in the room and each bookshelf takes up 80 square feet of space. If he reserves 160 square feet of space to use for a desk and some walking space, how many shelves can he put in the room?"""
    # Define the total square footage of the room and the reserved space
    total_space = 400
    reserved_space = 160

    # Calculate the available space for bookshelves
    available_space = total_space - reserved_space

    # Calculate the number of bookshelves that can fit in the available space
    shelves = available_space // 80

    # Return the result
    result = shelves
    return result

print(solution())