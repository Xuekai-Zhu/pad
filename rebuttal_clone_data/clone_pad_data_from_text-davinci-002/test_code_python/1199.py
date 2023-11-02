def solution():
    room_square_feet = 400
    shelf_square_feet = 80
    desk_and_walking_space_square_feet = 160
    bookcase_square_feet = room_square_feet - desk_and_walking_space_square_feet
    number_of_shelves = bookcase_square_feet / shelf_square_feet
    result = number_of_shelves
    return result

print(solution())