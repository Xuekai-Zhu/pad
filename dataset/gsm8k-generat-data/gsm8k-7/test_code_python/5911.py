def solution():
    num_floors = 20
    standard_height = 3
    added_height = 0.5  # height added to last 2 floors

    # Calculate the height of the first 18 floors (standard height)
    floor_height = standard_height * 18

    # Calculate the height of the last 2 floors (standard height + added height)
    last_floor_height = (standard_height + added_height) * 2

    # Calculate the total height of the building
    total_height = floor_height + last_floor_height
    result = total_height
    return result

print(solution())