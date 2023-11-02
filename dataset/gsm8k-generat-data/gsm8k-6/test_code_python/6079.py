def solution():
    # Calculate the number of small pink curlers
    pink_curlers = 16 / 4

    # Calculate the number of medium blue curlers
    blue_curlers = 2 * pink_curlers

    # Calculate the number of large green curlers
    green_curlers = 16 - pink_curlers - blue_curlers
    result = green_curlers
    return result

print(solution())