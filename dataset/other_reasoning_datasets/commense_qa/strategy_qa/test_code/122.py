def solution():
    mayflower_seafaring = True
    black_rock_desert_water = False
    if mayflower_seafaring and not black_rock_desert_water:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())