def solution():
    total_water_allowed = 1000
    water_for_drinking_cooking = 100
    water_for_pool = 10 * 10 * 6  # cubic feet of water needed to fill pool
    water_for_showers = 20  # gallons per shower

    # Calculate the remaining water after accounting for drinking/cooking and pool
    remaining_water = total_water_allowed - water_for_drinking_cooking - water_for_pool

    # Calculate the maximum number of showers Jerry can take
    num_showers = remaining_water / water_for_showers
    result = num_showers
    return result

print(solution())