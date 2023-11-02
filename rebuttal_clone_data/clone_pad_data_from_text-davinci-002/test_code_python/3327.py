def solution():
    initial_cost = 250
    gems_per_dollar = 100
    bonus_percentage = 20
    bonus_gems = initial_cost * (bonus_percentage / 100)
    total_gems = initial_cost * gems_per_dollar + bonus_gems
    result = total_gems
    return result

print(solution())