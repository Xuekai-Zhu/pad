def solution():
    
    initial_price = 220
    percent_increase = 15
    increase_amount = initial_price * (percent_increase / 100)
    new_price = increase_amount + initial_price
    result = new_price
    return result

print(solution())