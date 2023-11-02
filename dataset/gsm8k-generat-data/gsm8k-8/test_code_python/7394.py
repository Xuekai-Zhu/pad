def solution():
    # Calculate the number of tents on the east side
    east_tents = 2 * 100

    # Calculate the number of tents in the center of the camp
    center_tents = 4 * 100

    # Calculate the total number of tents
    total_tents = 100 + east_tents + center_tents + 200
    result = total_tents
    return result

print(solution())