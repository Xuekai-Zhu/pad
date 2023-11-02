def solution():
    """Nick is asking all his co-workers to chip in for a birthday gift for Sandra that costs $100. The boss agrees to contribute $15, and Todd volunteers to contribute twice as much since he always has to one-up everyone. If the remaining 5 employees (counting Nick) each pay an equal amount, how much do they each pay?"""
    # Define the cost of the gift and the boss's and Todd's contributions
    GIFT_COST = 100
    BOSS_CONTRIBUTION = 15
    TODD_CONTRIBUTION = 30

    # Determine the total remaining contributions needed
    TOTAL_CONTRIBUTIONS_NEEDED = GIFT_COST - BOSS_CONTRIBUTION - TODD_CONTRIBUTION

    # Determine the amount each of the remaining 5 employees needs to contribute
    EACH_CONTRIBUTION = TOTAL_CONTRIBUTIONS_NEEDED / 5

    # Display the amount each person needs to contribute
    result = EACH_CONTRIBUTION
    return result

print(solution())