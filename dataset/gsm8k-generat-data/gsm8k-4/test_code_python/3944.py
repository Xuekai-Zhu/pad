def solution():
    """Sara and Joe have a combined height of 120 inches. Joe is 6 inches more than double Sara's height. How tall is Joe?"""
    # Define the combined height of Sara and Joe
    combined_height = 120

    # Let s be Sara's height and j be Joe's height
    # Use the given information to set up a system of equations
    # s + j = 120 (equation 1)
    # j = 2s + 6 (equation 2)

    # Substitute equation 2 into equation 1 to eliminate j
    # s + (2s + 6) = 120
    # 3s = 114
    # s = 38

    # Substitute s = 38 into equation 2 to find j
    # j = 2(38) + 6
    # j = 82

    # Return Joe's height in inches
    result = 82
    return result

print(solution())