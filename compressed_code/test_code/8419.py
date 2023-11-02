def solution():
    
    money_spent = 250
    gems_per_dollar = 100
    total_gems = money_spent * gems_per_dollar
    bonus_percentage = 20
    bonus_gems = total_gems * (bonus_percentage / 100)
    total_gems += bonus_gems
    result = total_gems
    return result

print(solution())