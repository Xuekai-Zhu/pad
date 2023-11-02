def solution():
    selling_price = 220
    percent_increase = 15
    increase_amount = selling_price * (percent_increase / 100)
    new_price = selling_price + increase_amount
    result = new_price
    
    return result

print(solution())