def solution():
    
    costco_price = 8
    normal_store_price = 3
    normal_store_size = 16 
    gallon_size = 128 
    costco_price_per_ounce = costco_price / gallon_size
    normal_store_price_per_ounce = normal_store_price / normal_store_size
    savings_per_ounce = normal_store_price_per_ounce - costco_price_per_ounce
    savings_per_gallon = savings_per_ounce * gallon_size
    result = savings_per_gallon
    return result

print(solution())