def solution():
    
    air_conditioner_wattage = 900
    air_conditioner_hours_per_day = 8
    energy_wattage_per_hour = 900
    days = 30
    total_air_conditioner_wattage = air_conditioner_wattage * air_conditioner_hours_per_day * days
    total_energy_used_per_day = air_conditioner_wattage * days
    energy_saved_per_day = total_energy_used_per_day - total_energy_used_per_day
    energy_saved_in_30_days = energy_saved_per_day * 30
    result = energy_saved_in_30_days
    return result

print(solution())