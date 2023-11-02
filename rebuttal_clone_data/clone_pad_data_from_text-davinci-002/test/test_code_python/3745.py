def solution():
    lemon_orchards = 8
    orange_orchards = lemon_orchards / 2
    remaining_orchards = 16 - lemon_orchards - orange_orchards
    grapefruit_orchards = remaining_orchards / 2
    result = grapefruit_orchards
    
    return result

print(solution())