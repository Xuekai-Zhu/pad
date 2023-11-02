def solution():
    tiffany_speed = 6 / 3  # blocks per minute
    moses_speed = 12 / 8  # blocks per minute

    if tiffany_speed > moses_speed:
        result = tiffany_speed
    else:
        result = moses_speed

    return result

print(solution())