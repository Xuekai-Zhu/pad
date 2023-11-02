def solution():
    """Nancy bought a pie sliced it into 8 pieces. She gave 1/2 to Joe and Darcy, and she gave 1/4 to Carl. How many slices were left?"""
    total_slices = 8
    joe_darcy_slices = total_slices * (1/2)
    carl_slices = total_slices * (1/4)
    remaining_slices = total_slices - joe_darcy_slices - carl_slices
    result = remaining_slices
    return result

print(solution())