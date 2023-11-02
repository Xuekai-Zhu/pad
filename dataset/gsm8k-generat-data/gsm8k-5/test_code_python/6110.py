def solution():
    hours_worked = 8  # Ginger worked for 8 hours outside
    water_per_hour = 2  # Ginger drank 2 cups of water every hour
    water_drunk = hours_worked * water_per_hour  # Ginger drank this many cups of water

    water_for_plants = 5 * water_per_hour  # Ginger poured 5 full water bottles over her new plants

    total_water_used = water_drunk + water_for_plants  # Total cups of water Ginger used that day

    result = total_water_used
    return result

print(solution())