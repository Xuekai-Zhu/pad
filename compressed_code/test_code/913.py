def solution():
    
    room_size = 400
    reserved_space = 160
    shelf_size = 80
    max_shelves = (room_size - reserved_space) // shelf_size
    result = max_shelves
    return result

print(solution())