def solution():
    
    total_earned = 400
    cost_of_ingredients = 100
    remaining_money = total_earned - cost_of_ingredients
    donations = remaining_money / 2 + 10
    result = donations
    return result

print(solution())