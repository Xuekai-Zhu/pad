def solution():
    # Determine how many flowers contain each color and their overlaps
    yellow = 13 + 17 - 44
    red = 17 + 14 - 44
    white = 13 + 14 - 44

    # Calculate the difference between red and white flowers
    diff = red - white

    # Return the difference
    result = diff
    return result

print(solution())