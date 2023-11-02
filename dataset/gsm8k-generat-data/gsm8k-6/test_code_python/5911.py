def solution():
    # Calculate the height of the first 18 floors
    height_first_18_floors = 18 * 3  # each floor is 3 meters high

    # Calculate the height of the last two floors
    height_last_two_floors = 2 * (3 + 0.5)  # last two floors are each 0.5 meters higher

    # Calculate the total height of the building
    total_height = height_first_18_floors + height_last_two_floors
    result = total_height
    return result

print(solution())