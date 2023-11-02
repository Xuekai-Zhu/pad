def solution():
    total_gifts = 12
    roll1_gifts = 3
    roll2_gifts = 5
    rolls_used = 2

    # Calculate the total gifts wrapped using the first two rolls of paper
    total_gifts_wrapped = roll1_gifts + roll2_gifts

    # Calculate the remaining gifts to be wrapped
    remaining_gifts = total_gifts - total_gifts_wrapped

    # Calculate the number of gifts wrapped using the third roll of paper
    roll3_gifts = remaining_gifts / (rolls_used + 1)

    result = roll3_gifts
    return result

print(solution())