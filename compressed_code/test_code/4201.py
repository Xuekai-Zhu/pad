def solution():
    
    original_price = 40
    pack_size = 4
    total_price = original_price * 1.3
    price_per_type = total_price / pack_size
    result = price_per_type
    return result

print(solution())