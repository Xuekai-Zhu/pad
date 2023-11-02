def solution():
    # Calculate the total vertical distance between the riverbed and the peak of the hill
    total_distance = 300 * 4  # depth is a quarter of the vertical distance

    # Calculate the height of the hill by subtracting the depth from the total distance
    hill_height = total_distance - 300
    result = hill_height
    return result

print(solution())