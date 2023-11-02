def solution():
    initial_number_of_cattle = 340
    original_sale_price = 204000
    sick_cattle = 172
    lower_price = 150000
    total_cattle = initial_number_of_cattle - sick_cattle
    original_total_sale_price = original_sale_price * total_cattle
    lower_total_sale_price = lower_price * total_cattle
    loss = original_total_sale_price - lower_total_sale_price
    result = loss
    
    return result

print(solution())