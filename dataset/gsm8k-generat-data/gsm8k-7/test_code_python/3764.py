def solution():
    resistance_per_band = 5
    num_bands = 2
    weight_dumbbell = 10

    # Calculate the total resistance added by the bands
    total_resistance = resistance_per_band * num_bands * 2  # double up both sets of bands

    # Calculate the total weight that Lindsey will squat
    total_weight = total_resistance + weight_dumbbell
    result = total_weight
    return result

print(solution())