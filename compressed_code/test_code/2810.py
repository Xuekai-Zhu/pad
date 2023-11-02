def solution():
    
    steak_price_per_pound = 7
    pounds_of_steak = 2
    total_price = steak_price_per_pound * pounds_of_steak
    payment = 20
    change = payment - total_price
    result = change
    return result

print(solution())