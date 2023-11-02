def solution():
    # Calculate the number of blue chips
    blue_chips = 60 / 6

    # Calculate the number of green chips
    green_chips = 60 - blue_chips - 34
    result = green_chips
    return result

print(solution())