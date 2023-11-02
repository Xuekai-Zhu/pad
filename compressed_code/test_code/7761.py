def solution():
    
    total_items = 11
    total_amount = 69
    shirts = 4
    shirt_price = 5
    dress_price = (total_amount - (shirts * shirt_price)) / (total_items - shirts)
    result = dress_price
    return result

print(solution())