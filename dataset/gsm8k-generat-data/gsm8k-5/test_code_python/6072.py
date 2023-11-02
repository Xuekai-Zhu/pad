def solution():
    shampoo_per_day = 1  # Sarah uses 1 ounce of shampoo per day
    conditioner_per_day = 0.5 * shampoo_per_day  # Sarah uses half as much conditioner as shampoo
    days_per_week = 7  # There are 7 days in a week
    weeks = 2  # Sarah wants to know the total volume of shampoo and conditioner she will use in 2 weeks

    # Calculate the total volume of shampoo and conditioner Sarah will use in 2 weeks
    total_shampoo = shampoo_per_day * days_per_week * weeks
    total_conditioner = conditioner_per_day * days_per_week * weeks
    total_volume = total_shampoo + total_conditioner
    result = total_volume
    return result

print(solution())