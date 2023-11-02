def solution():
    # Calculate the number of shrimp caught by Austin's trap
    austin_shrimp = 26 - 8

    # Calculate the total shrimp caught by all three traps
    total_shrimp = 26 + austin_shrimp + ((26 + austin_shrimp) / 2)

    # Calculate the total earnings of the group
    total_earnings = (total_shrimp / 11) * 7

    # Calculate the earnings per boy
    earnings_per_boy = total_earnings / 3
    result = earnings_per_boy
    return result

print(solution())