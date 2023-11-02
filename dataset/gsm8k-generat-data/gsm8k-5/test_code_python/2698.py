def solution():
    total_walls = (5 * 4) + (4 * 5)  # Total number of walls in the house
    num_people = 5  # There are 5 people in Amanda's family, including herself

    # Calculate the number of walls each person should paint
    walls_per_person = total_walls // num_people
    result = walls_per_person
    return result

print(solution())