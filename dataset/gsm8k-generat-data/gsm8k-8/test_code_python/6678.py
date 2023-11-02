def solution():
    total_orchards = 16
    lemon_orchards = 8
    orange_orchards = lemon_orchards / 2
    lime_and_grapefruit_orchards = total_orchards - lemon_orchards - orange_orchards

    grapefruit_orchards = lime_and_grapefruit_orchards / 2
    result = grapefruit_orchards
    return result

print(solution())