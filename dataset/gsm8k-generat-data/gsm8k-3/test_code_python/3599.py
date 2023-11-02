def solution():
    """Victor, Austin, and Brian made traps to catch shrimp. Victor's trap caught 26 shrimp and Austin's trap caught 8 less than Victor's. Brian's trap caught half of Victor and Austin's total number of shrimp. If the boys then sold their shrimp for $7 for every 11 tails of shrimp and then divided their earnings equally amongst themselves, how much money does each boy make?"""
    # Calculate the number of shrimp caught by Austin's trap
    austin_shrimp = 26 - 8

    # Calculate the total number of shrimp caught by all three traps
    total_shrimp = 26 + austin_shrimp + (0.5 * (26 + austin_shrimp))

    # Calculate the total earnings from selling the shrimp
    total_earnings = (total_shrimp // 11) * 7

    # Calculate each boy's share of the earnings
    per_boy_earnings = total_earnings // 3

    # Display each boy's earnings
    result = per_boy_earnings
    return result

print(solution())