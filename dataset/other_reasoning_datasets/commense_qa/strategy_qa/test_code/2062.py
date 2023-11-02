def solution():
    drone_price = 1000
    coin_price_range = [2283, 4933]
    if max(coin_price_range) >= drone_price:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())