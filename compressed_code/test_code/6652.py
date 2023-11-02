def solution():
    
    starting_money = 400
    money_to_mom = starting_money * (1/4)
    money_for_clothes = starting_money * (1/8)
    money_to_charity = starting_money * (1/5)
    money_remaining = starting_money - money_to_mom - money_for_clothes - money_to_charity
    result = money_remaining
    return result

print(solution())