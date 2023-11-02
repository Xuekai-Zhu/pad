def solution():
    retail_price = 36
    markup = 80
    wholesale_price = retail_price / (1 + (markup / 100))
    result = wholesale_price
    return result

print(solution())