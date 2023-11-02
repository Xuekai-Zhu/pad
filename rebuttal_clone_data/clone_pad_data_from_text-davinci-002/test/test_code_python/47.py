def solution():
    
    cost_per_ounce = 0.25
    money_brought = 2
    money_left = 0.50
    cost_of_soda = money_brought - money_left
    ounces_bought = cost_of_soda / cost_per_ounce
    result = ounces_bought
    return result

print(solution())