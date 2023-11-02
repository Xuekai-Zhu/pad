def solution():
    # Calculate the total number of walls in the house
    total_walls = 5*4 + 4*5

    # Divide the total number of walls by the number of people in Amanda's family
    walls_per_person = total_walls / 5

    result = walls_per_person
    return result

print(solution())