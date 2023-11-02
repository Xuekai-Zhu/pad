def solution():
    total_clovers = 200
    three_petals = 0.75 * total_clovers
    two_petals = 0.24 * total_clovers
    four_petals = 0.01 * total_clovers

    # Calculate the total earnings from picking 3-petal clovers
    earnings_three_petals = three_petals * 0.01

    # Calculate the total earnings from picking 2-petal clovers
    earnings_two_petals = two_petals * 0.01

    # Calculate the total earnings from picking 4-petal clovers
    earnings_four_petals = four_petals * 0.01

    # Calculate the total earnings from picking all clovers
    total_earnings = earnings_three_petals + earnings_two_petals + earnings_four_petals

    result = total_earnings
    return result

print(solution())