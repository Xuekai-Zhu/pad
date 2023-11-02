def solution():
    # Define the distances between stores
    first_to_second = 6
    second_to_third = 2/3 * first_to_second

    # Calculate the total distance of the trip
    total_distance = first_to_second + second_to_third + first_to_second + 4 + 4

    result = total_distance
    return result

print(solution())