def solution():
    
    hens = 10
    egg_price = 3 / 12
    total_egg_count = 120 / egg_price
    egg_per_week_per_hen = total_egg_count / (hens * 4)
    result = egg_per_week_per_hen
    return result

print(solution())