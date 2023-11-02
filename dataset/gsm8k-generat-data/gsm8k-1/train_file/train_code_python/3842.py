def solution():
    """Nancy bought a pie sliced it into 8 pieces. She gave 1/2 to Joe and Darcy, and she gave 1/4 to Carl. How many slices were left?"""
    total_slices = 8
    slices_given_away = (1/2 * total_slices) + (1/2 * total_slices) + (1/4 * total_slices)
    slices_left = total_slices - slices_given_away
    result = slices_left
    return result

print(solution())