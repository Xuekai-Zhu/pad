def solution():
    # Calculate total earnings so far and pounds picked on Tuesday
    earnings = 2*8 + 2*(3*8)
    pounds_picked = 8 + 3*8

    # Calculate how much he needs to make on Thursday
    remaining_earnings = 100 - earnings
    pounds_to_pick = remaining_earnings / 2

    # Account for pounds picked on Tuesday and return result
    result = pounds_to_pick - pounds_picked
    return result

print(solution())