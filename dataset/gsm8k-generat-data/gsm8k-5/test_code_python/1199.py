def solution():
    total_space = 400  # The room has 400 square feet of space
    reserved_space = 160  # 160 square feet of space will be reserved for a desk and walking space
    available_space = total_space - reserved_space  # This is how much space is available for bookshelves
    shelf_space = 80  # Each bookshelf takes up 80 square feet of space

    # Calculate how many bookshelves can fit in the available space
    num_shelves = available_space // shelf_space
    result = num_shelves
    return result

print(solution())