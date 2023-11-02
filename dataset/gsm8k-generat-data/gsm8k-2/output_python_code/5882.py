def solution():
    """Iain has 200 pennies. He realizes that 30 of his pennies are older than he is. If he wishes to get rid of these pennies and then throw out 20% of his remaining pennies, how many will he have left?"""
    total_pennies = 200
    old_pennies = 30
    remaining_pennies = total_pennies - old_pennies
    throw_away_amount = int(0.2 * remaining_pennies)
    remaining_pennies = remaining_pennies - throw_away_amount
    result = remaining_pennies
    return result

print(solution())