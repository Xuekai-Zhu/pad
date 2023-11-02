def solution():
    # Calculate the total number of spaces occupied by the caravans
    spaces_per_caravan = 2
    total_spaces = spaces_per_caravan * 3

    # Calculate the number of remaining spaces for vehicles
    remaining_spaces = 30 - total_spaces
    result = remaining_spaces
    return result

print(solution())