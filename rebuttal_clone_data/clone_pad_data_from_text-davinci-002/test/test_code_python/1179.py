def solution():
    total_chips = 60
    blue_chips = total_chips / 6
    red_chips = 34
    green_chips = total_chips - red_chips - blue_chips
    result = green_chips
    return result

print(solution())