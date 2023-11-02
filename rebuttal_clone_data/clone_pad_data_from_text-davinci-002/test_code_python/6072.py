def solution():
    ounces_per_day = 1
    ounces_per_week = 7
    conditioner_ratio = 0.5
    shampoo_volume = ounces_per_day * ounces_per_week
    conditioner_volume = conditioner_ratio * shampoo_volume
    total_volume = shampoo_volume + conditioner_volume
    result = total_volume
    return result

print(solution())