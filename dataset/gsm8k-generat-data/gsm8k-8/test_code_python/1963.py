def solution():
    # Calculate Christine's commission earnings
    commission_earnings = 0.12 * 24000

    # Calculate the amount allocated for personal needs
    personal_needs = 0.6 * commission_earnings

    # Calculate the amount saved
    saved_amount = commission_earnings - personal_needs
    result = saved_amount
    return result

print(solution())