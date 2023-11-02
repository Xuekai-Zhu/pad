def solution():
    # Calculate the height of the first 18 floors
    height_first_18_floors = 18 * 3  # Each of the first 18 floors is 3 meters high

    # Calculate the height of the 19th and 20th floors
    height_last_two_floors = 2 * (3 + 0.5)  # Each of the last two floors is 0.5 meters higher than the rest

    # Calculate the total height of the building
    total_height = height_first_18_floors + height_last_two_floors
    result = total_height
    return result

print(solution())