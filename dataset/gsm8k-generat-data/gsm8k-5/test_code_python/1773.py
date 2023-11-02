def solution():
    total_gifts = 12
    roll1_gifts = 3
    roll2_gifts = 5

    # Calculate the number of gifts wrapped with the first two rolls of paper
    wrapped_gifts = roll1_gifts + roll2_gifts

    # Calculate the number of gifts wrapped with the third roll of paper
    remaining_gifts = total_gifts - wrapped_gifts
    roll3_gifts = remaining_gifts // 3

    result = roll3_gifts
    return result

print(solution())