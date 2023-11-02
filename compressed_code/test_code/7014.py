def solution():
    
    initial_budget = 60
    percent_increase = 20
    new_price = initial_budget * (1 + (percent_increase / 100))
    smaller_price = new_price * (3 / 4)
    money_left = initial_budget - smaller_price
    result = money_left
    return result

print(solution())