def solution():
    money_per_bag = 4
    money_earned = 68
    bags_raked_on_monday = 5
    bags_raked_on_tuesday = 3
    bags_raked_on_wednesday = money_earned - (money_per_bag * bags_raked_on_monday + bags_raked_on_tuesday)
    result = bags_raked_on_wednesday
    return result

print(solution())