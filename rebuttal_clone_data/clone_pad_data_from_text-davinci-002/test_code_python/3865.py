def solution():
    initial_amount = 20
    Money_from_mom = initial_amount * 2
    total_amount = Money_from_mom + initial_amount
    cost_of_cupcakes = 10 * 1.50
    cost_of_cookies = 5 * 3
    total_cost = cost_of_cupcakes + cost_of_cookies
    money_left = total_amount - total_cost
    result = money_left
    
    return result

print(solution())