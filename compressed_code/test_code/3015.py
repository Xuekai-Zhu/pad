def solution():
    
    larger_box_price_per_ounce = 4.8 / 30
    smaller_box_price_per_ounce = 3.4 / 20
    if smaller_box_price_per_ounce < larger_box_price_per_ounce:
        result = int(smaller_box_price_per_ounce * 100)
    else:
        result = int(larger_box_price_per_ounce * 100)
    return result

print(solution())