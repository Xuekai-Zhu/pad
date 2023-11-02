def solution():
    # Calculate the number of gifts wrapped with the first two rolls of paper
    gifts_wrapped_first_two_rolls = (3 * 1) + (5 * 1)  # 1 roll to wrap 3 gifts, 1 roll to wrap 5 other gifts

    # Calculate the number of gifts wrapped with the third roll of paper
    gifts_wrapped_third_roll = 12 - gifts_wrapped_first_two_rolls

    result = gifts_wrapped_third_roll
    return result

print(solution())