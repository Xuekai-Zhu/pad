def solution():
    safe_amount = 500
    energy_drink_caffeine = 120
    num_energy_drinks = 4

    total_caffeine = energy_drink_caffeine * num_energy_drinks
    remaining_caffeine = safe_amount - total_caffeine
    result = remaining_caffeine
    return result

print(solution())