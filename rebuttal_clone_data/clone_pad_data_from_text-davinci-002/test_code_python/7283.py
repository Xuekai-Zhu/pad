def solution():
    bean_seedlings = 64
    pumpkin_seeds = 84
    radishes = 48
    bean_rows_per_bed = 2
    pumpkin_rows_per_bed = 2
    radish_rows_per_bed = 2
    bean_beds = bean_seedlings / (bean_rows_per_bed * 8)
    pumpkin_beds = pumpkin_seeds / (pumpkin_rows_per_bed * 7)
    radish_beds = radishes / (radish_rows_per_bed * 6)
    total_beds = bean_beds + pumpkin_beds + radish_beds
    result = total_beds
    return result

print(solution())