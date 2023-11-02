def solution():
    
    candy_bar_cost = 3 * 10  
    lollipop_cost = 25  
    total_cost = 4 * candy_bar_cost + lollipop_cost
    total_money = 19 * 10 + 6 * 25  
    money_left = total_money - total_cost
    result = money_left
    return result

print(solution())