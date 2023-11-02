def solution():
    # Define the known values
    base_height = 300
    ratio = 4

    # Calculate the total vertical distance
    total_distance = ratio * base_height

    # Calculate the height of the hill by subtracting the base height
    hill_height = total_distance - base_height
    result = hill_height
    return result

print(solution())