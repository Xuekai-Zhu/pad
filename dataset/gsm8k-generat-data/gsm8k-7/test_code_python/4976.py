def solution():
    num_glasses = 10
    glass_volume = 6  # in ounces
    fill_percent = 0.8  # 4/5 full
    empty_percent = 1 - fill_percent

    # Calculate the volume of water needed to fill all glasses to the brim
    total_water_needed = num_glasses * glass_volume * empty_percent

    result = total_water_needed
    return result

print(solution())