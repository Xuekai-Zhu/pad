def solution():
    num_shots = 8
    shot_size = 1.5 # in ounces
    purity = 0.5 # 50% purity

    # Calculate the total amount of vodka consumed in ounces
    total_vodka = num_shots * shot_size

    # Calculate the total amount of pure alcohol consumed in ounces
    total_pure_alcohol = total_vodka * purity

    result = total_pure_alcohol
    return result

print(solution())