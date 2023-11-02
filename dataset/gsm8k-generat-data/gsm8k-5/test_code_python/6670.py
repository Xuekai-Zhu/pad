def solution():
    total_chips = 10 / 0.1  # There are 10 times the number of chips in the jar as there are blue chips
    white_chips = 0.5 * total_chips  # 50% of the chips are white 
    blue_chips = 3
    green_chips = total_chips - white_chips - blue_chips  # The rest of the chips are green
    result = green_chips
    return result

print(solution())