def solution():
    # Define the number of spots on the left side
    left_spots = 16

    # Calculate the number of spots on the right side
    right_spots = 3 * left_spots + 7

    # Calculate the total number of spots
    total_spots = left_spots + right_spots

    result = total_spots
    return result

print(solution())