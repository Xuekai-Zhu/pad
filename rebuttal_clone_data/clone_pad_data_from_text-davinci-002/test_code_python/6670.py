def solution():
    total_chips = 100
    blue_chips = total_chips * 0.10
    white_chips = total_chips * 0.50
    green_chips = total_chips - blue_chips - white_chips
    result = green_chips
    return result

print(solution())