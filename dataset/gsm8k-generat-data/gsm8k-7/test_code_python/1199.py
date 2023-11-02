def solution():
    total_space = 400
    reserved_space = 160
    shelf_space = 80

    # Calculate the total available space for bookshelves
    available_space = total_space - reserved_space

    # Calculate the maximum number of bookshelves that can fit in the available space
    num_shelves = available_space // shelf_space
    result = num_shelves
    return result

print(solution())