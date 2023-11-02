def solution():
    price_of_shirt = 60
    new_price_of_shirt = price_of_shirt * 0.8
    price_of_jacket = 90
    new_price_of_jacket = price_of_jacket * 0.8
    number_of_shirts = 5
    number_of_jackets = 10
    total_price = (new_price_of_shirt * number_of_shirts) + (new_price_of_jacket * number_of_jackets)
    result = total_price
    return result

print(solution())