def solution():
    side_length = 6
    density = 19
    price_per_gram = 60
    volume = side_length**3
    weight = volume * density
    sale_price = price_per_gram * weight * 1.5
    profit = sale_price - (price_per_gram * weight)
    result = profit
    return result

print(solution())