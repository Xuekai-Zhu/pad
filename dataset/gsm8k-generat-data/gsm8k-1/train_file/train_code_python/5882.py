def solution():
    """Iain has 200 pennies. He realizes that 30 of his pennies are older than he is. If he wishes to get rid of these pennies and then throw out 20% of his remaining pennies, how many will he have left?"""
    total_pennies = 200
    older_pennies = 30
    remaining_pennies = total_pennies - older_pennies
    thrown_away_pennies = int(remaining_pennies * 0.2)
    final_pennies = remaining_pennies - thrown_away_pennies
    result = final_pennies
    return result

print(solution())