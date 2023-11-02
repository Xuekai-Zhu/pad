def solution():
    # Calculate the total space available for bookshelves
    bookshelf_space = 400 - 160

    # Calculate the number of shelves that can fit in the room
    num_shelves = bookshelf_space // 80
    result = num_shelves
    return result

print(solution())