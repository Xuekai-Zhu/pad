def solution():
    
    room_space = 400
    reserved_space = 160
    bookshelf_space = 80
    available_space = room_space - reserved_space
    shelves = available_space // bookshelf_space
    result = shelves
    return result

print(solution())