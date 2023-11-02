def solution():
    # Calculate the total number of chips in the jar
    total_chips = 3 / 0.1  # 3 blue chips are 10% of the entire chips

    # Calculate the number of white chips in the jar
    white_chips = 0.5 * total_chips  # 50% of the chips are white

    # Calculate the number of green chips in the jar
    green_chips = total_chips - (3 + white_chips)  # the rest are green chips

    result = green_chips
    return result

print(solution())