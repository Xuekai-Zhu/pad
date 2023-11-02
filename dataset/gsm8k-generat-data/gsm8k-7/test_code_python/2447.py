def solution():
    num_blankets = 14
    blankets_used = num_blankets / 2 # Half of the blankets are used
    warming_effect_per_blanket = 3

    # Calculate the total warming effect of all blankets used
    total_warming_effect = blankets_used * warming_effect_per_blanket

    result = total_warming_effect
    return result

print(solution())