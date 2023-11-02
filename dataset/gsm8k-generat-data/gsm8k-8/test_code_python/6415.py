def solution():
    # Define variables
    total_capacity = 21
    life_jacket_capacity = total_capacity - 7
    num_people_with_life_jackets = 8

    # Calculate the capacity with life jackets
    capacity_with_life_jackets = life_jacket_capacity - num_people_with_life_jackets

    # Calculate the total capacity
    total_capacity = capacity_with_life_jackets + num_people_with_life_jackets

    result = total_capacity
    return result

print(solution())