def solution():
    """Victor, Austin, and Brian made traps to catch shrimp. Victor's trap caught 26 shrimp and Austin's trap caught 8 less than Victor's. Brian's trap caught half of Victor and Austin's total number of shrimp. If the boys then sold their shrimp for $7 for every 11 tails of shrimp and then divided their earnings equally amongst themselves, how much money does each boy make?"""
    # Number of shrimp caught by each boy
    victor_shrimp = 26
    austin_shrimp = victor_shrimp - 8
    brian_shrimp = (victor_shrimp + austin_shrimp) / 2

    # Total number of shrimp caught
    total_shrimp = victor_shrimp + austin_shrimp + brian_shrimp

    # Total number of tails of shrimp
    total_tails = total_shrimp * 2

    # Total earnings from selling shrimp
    total_earnings = (total_tails // 11) * 7

    # Earnings per boy
    earnings_per_boy = total_earnings // 3

    result = earnings_per_boy
    return result

print(solution())