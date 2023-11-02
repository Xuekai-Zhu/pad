def solution():
    """An archer needs to practice.  He intends to shoot 200 shots 4 days a week.  He is able to recover 20% of his arrows.  The arrows he uses cost $5.5 per arrow.  His team agrees to pay for 70% of the cost of his arrows.  How much does he spend for arrows a week?"""
    # Define the number of shots per week and the percentage of arrows he recovers
    SHOTS_PER_WEEK = 200 * 4
    ARROW_RECOVERY_PERCENTAGE = 0.2

    # Calculate the number of arrows he needs to buy per week
    total_arrows = SHOTS_PER_WEEK / (1 - ARROW_RECOVERY_PERCENTAGE)

    # Calculate his total cost for arrows per week
    ARROW_COST = 5.5
    TEAM_COVERAGE_PERCENTAGE = 0.7
    total_arrow_cost = total_arrows * ARROW_COST * (1 - TEAM_COVERAGE_PERCENTAGE)

    # Display his total cost for arrows per week
    result = total_arrow_cost
    return result

print(solution())