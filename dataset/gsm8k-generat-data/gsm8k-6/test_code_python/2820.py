def solution():
    # Calculate the total number of spots on the cow
    left_spots = 16
    right_spots = 3*left_spots + 7
    total_spots = left_spots + right_spots
    result = total_spots
    return result

print(solution())