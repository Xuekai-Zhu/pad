def solution():
    """The central Texas countryside contains many toads that come out at night. For every green toad, there are 25 brown toads, and one-quarter of the brown toads are spotted. If there are 50 spotted brown toads per acre, how many green toads are there per acre?"""
    spotted_brown_toads = 50
    brown_toads = spotted_brown_toads * 4
    green_toads = brown_toads / 25
    total_toads = green_toads + brown_toads
    result = green_toads
    return result

print(solution())