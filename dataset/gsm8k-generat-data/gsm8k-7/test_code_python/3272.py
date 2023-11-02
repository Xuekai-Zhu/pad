def solution():
    old_water_per_flush = 5
    new_water_per_flush = old_water_per_flush * 0.2 

    num_flushes_per_day = 15
    days_in_june = 30

    old_water_usage_per_day = old_water_per_flush * num_flushes_per_day
    new_water_usage_per_day = new_water_per_flush * num_flushes_per_day

    water_saved_per_day = old_water_usage_per_day - new_water_usage_per_day
    water_saved_in_june = water_saved_per_day * days_in_june
    result = water_saved_in_june
    return result

print(solution())