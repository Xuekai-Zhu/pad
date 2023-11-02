def solution():
    """Billy has $25 less than twice the money Sam has. If Sam has $75, how much money do they have together?"""
    # Define Sam's money
    sam_money = 75

    # Calculate Billy's money
    billy_money = 2 * sam_money - 25

    # Calculate the total money they have together
    total_money = sam_money + billy_money

    result = total_money
    return result

print(solution())