def solution():
    """Billy has $25 less than twice the money Sam has. If Sam has $75, how much money do they have together?"""
    # Define the amount of money Sam has
    sam_money = 75

    # Calculate the amount of money Billy has
    billy_money = 2 * sam_money - 25

    # Calculate the total amount of money they have together
    total_money = sam_money + billy_money

    # Display the total amount of money they have together
    result = total_money
    return result

print(solution())