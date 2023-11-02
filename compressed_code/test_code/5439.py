def solution():
    
    starting_money = 600
    gas_spending = starting_money / 3
    money_left = starting_money - gas_spending
    food_spending = money_left / 4
    money_left -= food_spending
    result = money_left
    return result

print(solution())