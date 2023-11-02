def solution():
    
    original_price = 100
    percent_decrease = 20
    decrease_amount = original_price * (percent_decrease / 100)
    new_price = original_price - decrease_amount
    result = new_price
    return result

print(solution())