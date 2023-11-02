def solution():
    
    big_bottle_ounces = 30
    big_bottle_price = 2700
    small_bottle_ounces = 6
    small_bottle_price = 600
    equal_volume_ounces = big_bottle_ounces / small_bottle_ounces
    equal_volume_price = equal_volume_ounces * small_bottle_price
    pesetas_saved = equal_volume_price - big_bottle_price
    result = pesetas_saved
    return result

print(solution())