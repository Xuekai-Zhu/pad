def solution():
    # Calculate the speed of Tiffany (blocks per minute)
    tiffany_speed = 6 / 3

    # Calculate the speed of Moses (blocks per minute)
    moses_speed = 12 / 8

    # Determine which runner has a higher average speed
    if tiffany_speed > moses_speed:
        result = tiffany_speed
    else:
        result = moses_speed
    return result

print(solution())