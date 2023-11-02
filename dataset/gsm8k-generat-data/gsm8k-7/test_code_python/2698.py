def solution():
    num_people = 5
    num_rooms = 9
    num_walls = (5 * 4) + (4 * 5)  # 5 rooms with 4 walls and 4 rooms with 5 walls

    # Calculate the number of walls that each person should paint
    num_walls_per_person = num_walls / num_people
    result = num_walls_per_person
    return result

print(solution())