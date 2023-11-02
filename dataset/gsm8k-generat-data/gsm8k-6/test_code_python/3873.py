def solution():
    # Calculate the speed of Tiffany and Moses
    tiffany_speed = 6 / 3  # Tiffany runs 6 blocks in 3 minutes
    moses_speed = 12 / 8  # Moses runs 12 blocks in 8 minutes

    # Find the runner with the higher average speed
    if tiffany_speed > moses_speed:
        result = tiffany_speed
    else:
        result = moses_speed
    return result

print(solution())