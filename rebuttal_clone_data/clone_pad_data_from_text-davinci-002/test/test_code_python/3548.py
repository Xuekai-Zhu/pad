def solution():
    large_birdhouses = 2
    medium_birdhouses = 2
    small_birdhouses = 3
    price_large = 22
    price_medium = 16
    price_small = 7
    total_price = (large_birdhouses * price_large) + (medium_birdhouses * price_medium) + (small_birdhouses * price_small)
    result = total_price
    return result

print(solution())