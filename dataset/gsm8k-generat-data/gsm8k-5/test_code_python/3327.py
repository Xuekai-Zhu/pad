def solution():
    gems_per_dollar = 100  # The game gives 100 gems for every dollar spent
    amount_spent = 250  # Tom spent $250
    total_gems = gems_per_dollar * amount_spent  # Calculate the total number of gems before the bonus
    bonus_percentage = 20  # Tom received a 20% bonus on top of his purchase
    bonus_multiplier = 1 + (bonus_percentage/100)  # Calculate the bonus multiplier
    final_gems = total_gems * bonus_multiplier  # Calculate the total number of gems with the bonus
    result = final_gems
    return result

print(solution())