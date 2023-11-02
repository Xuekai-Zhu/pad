def solution():
    # Calculate the amount of money in Karen's and Christopher's piggy banks
    karen_money = 32 * 0.25  # each quarter is worth $0.25
    christopher_money = 64 * 0.25

    # Calculate how much more money Christopher has
    more_money = christopher_money - karen_money
    result = more_money
    return result

print(solution())