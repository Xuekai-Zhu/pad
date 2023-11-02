def solution():
    # Calculate the total earnings from this Sunday
    trout = 0.6 * 5
    blue_gill = 5 - trout
    total_earnings = (trout * 5) + (blue_gill * 4)

    # Calculate the total earnings so far
    total_earnings += 35

    # Calculate how much more Bucky needs to save
    remaining_amount = 60 - total_earnings
    result = remaining_amount
    return result

print(solution())