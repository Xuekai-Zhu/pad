def solution():
    initial_money = 400
    money_given_to_mom = initial_money / 4
    money_spent_on_clothes = initial_money / 8
    money_given_to_charity = initial_money / 5
    money_kept = initial_money - money_given_to_mom - money_spent_on_clothes - money_given_to_charity
    result = money_kept
    
    return result

print(solution())