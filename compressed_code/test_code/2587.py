def solution():
    
    dollars_spent = 250
    gems_per_dollar = 100
    total_gems = dollars_spent * gems_per_dollar
    bonus_percentage = 0.2
    bonus_gems = total_gems * bonus_percentage
    total_gems += bonus_gems
    result = total_gems
    return result

print(solution())