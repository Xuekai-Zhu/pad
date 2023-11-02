def solution():
    """Isabella has three times as many green houses as yellow houses. She also has 40 fewer yellow houses than red houses.
    If she has 90 green houses, how many of her houses are not yellow?"""
    
    green_houses = 90
    yellow_houses = green_houses / 3
    red_houses = yellow_houses + 40
    not_yellow_houses = green_houses + red_houses
    result = not_yellow_houses
    return result

print(solution())