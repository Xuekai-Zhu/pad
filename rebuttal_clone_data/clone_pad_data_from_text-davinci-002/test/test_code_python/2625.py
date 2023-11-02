def solution():
    baby_carrots = 47
    goats = 4
    carrots_per_goat = baby_carrots // goats
    carrots_left_over = baby_carrots % goats
    result = carrots_left_over
    return result

print(solution())