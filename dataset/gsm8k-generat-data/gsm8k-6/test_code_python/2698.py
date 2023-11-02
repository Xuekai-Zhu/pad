def solution():
    # Calculate total number of walls in the house
    total_walls = (5 * 4) + (4 * 5)  # 5 rooms with 4 walls each and 4 rooms with 5 walls each

    # Calculate number of walls each person should paint to divide work equally
    walls_per_person = total_walls / 5

    result = walls_per_person
    return result

print(solution())