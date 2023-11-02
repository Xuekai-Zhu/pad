def solution():
    side_length = 3
    silver_weight = 6
    silver_price = 25
    profit_margin = 10
    volume = side_length ** 3
    total_silver_weight = volume * silver_weight
    total_silver_value = total_silver_weight * silver_price
    total_price = total_silver_value * (1 + (profit_margin / 100))
    result = total_price
    return result

print(solution())