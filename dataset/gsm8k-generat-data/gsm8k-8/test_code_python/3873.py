def solution():
    # Calculate the speed of Tiffany
    tiffany_speed = 6 / 3

    # Calculate the speed of Moses
    moses_speed = 12 / 8

    # Find the runner with the higher average speed
    if tiffany_speed > moses_speed:
        result = tiffany_speed
    else:
        result = moses_speed

    return result

print(solution())