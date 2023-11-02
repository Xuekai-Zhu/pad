def solution():
    
    num_people = 5
    num_rooms = 9
    num_four_walls_rooms = 5
    num_five_walls_rooms = 4
    num_walls = (num_four_walls_rooms * 4) + (num_five_walls_rooms * 5)
    walls_per_person = num_walls // num_people
    result = walls_per_person
    return result

print(solution())