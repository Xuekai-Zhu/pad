def solution():
    
    initial_price = 400
    decrease_percent = 15
    increase_percent = 40
    decrease_amount = initial_price * (decrease_percent / 100)
    decreased_price = initial_price - decrease_amount
    increase_amount = decreased_price * (increase_percent / 100)
    final_price = decreased_price + increase_amount
    result = final_price
    return result

print(solution())