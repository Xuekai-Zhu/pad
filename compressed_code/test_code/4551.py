def solution():
    
    total_pennies = 200
    old_pennies = 30
    remaining_pennies = total_pennies - old_pennies
    throw_away_amount = int(0.2 * remaining_pennies)
    remaining_pennies = remaining_pennies - throw_away_amount
    result = remaining_pennies
    return result

print(solution())