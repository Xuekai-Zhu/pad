def solution():
    
    first_bear_price = 4.00
    discount = 0.50
    additional_bears = 100
    additional_bear_price = first_bear_price - discount
    total_price = (first_bear_price + additional_bear_price * additional_bears)
    result = total_price
    return result

print(solution())