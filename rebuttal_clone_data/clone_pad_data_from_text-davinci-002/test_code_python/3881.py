def solution():
     price_large = 4.80
     price_small = 3.40
     ounces_large = 30
     ounces_small = 20
     price_large_per_ounce = price_large / ounces_large
     price_small_per_ounce = price_small / ounces_small
     better_value = min(price_large_per_ounce, price_small_per_ounce)
     result = better_value * 100
    return result

print(solution())