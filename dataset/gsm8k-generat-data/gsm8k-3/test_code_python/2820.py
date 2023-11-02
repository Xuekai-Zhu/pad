def solution():
    """Ruth is counting the number of spots on her cow. The cow has 16 spots on its left side and three times that number plus 7 on its right side. How many spots does it have total?"""
    # Define the number of spots on the left side
    left_spots = 16

    # Calculate the number of spots on the right side
    right_spots = 3 * left_spots + 7

    # Calculate the total number of spots
    total_spots = left_spots + right_spots

    # Display the total number of spots
    result = total_spots
    return result

print(solution())