def solution():
    
    retail_price = 36
    markup_percentage = 0.8
    wholesale_price = retail_price / (1 + markup_percentage)
    result = wholesale_price
    return result

print(solution())