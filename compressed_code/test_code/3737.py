def solution():
    
    money = 20
    spent_on_snacks = money * (1/5)
    remaining_money = money - spent_on_snacks
    spent_on_necessities = remaining_money * (3/4)
    remaining_money -= spent_on_necessities
    result = remaining_money
    return result

print(solution())