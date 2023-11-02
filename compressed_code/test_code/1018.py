def solution():
    
    total_saved = 36
    number_of_tires = 4
    sale_price = 75
    total_sale_price = sale_price * number_of_tires
    original_price_per_tire = (total_sale_price + total_saved) / number_of_tires
    result = original_price_per_tire
    return result

print(solution())