def solution():
    
    larger_box_cost = 4.8
    smaller_box_cost = 3.4
    larger_box_size = 30
    smaller_box_size = 20
    larger_box_price_per_ounce = larger_box_cost / larger_box_size
    smaller_box_price_per_ounce = smaller_box_cost / smaller_box_size
    if larger_box_price_per_ounce < smaller_box_price_per_ounce:
        result = int(larger_box_price_per_ounce * 100)
    else:
        result = int(smaller_box_price_per_ounce * 100)
    return result

print(solution())