def solution():
    shampoo_per_day = 1.0
    conditioner_per_day = 0.5

    num_days = 14

    # Calculate the total amount of shampoo used in 2 weeks
    total_shampoo_used = shampoo_per_day * num_days

    # Calculate the total amount of conditioner used in 2 weeks
    total_conditioner_used = conditioner_per_day * num_days

    # Calculate the total volume of shampoo and conditioner used
    total_volume_used = total_shampoo_used + total_conditioner_used
    result = total_volume_used
    return result

print(solution())