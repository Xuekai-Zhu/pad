def solution():
    
    koolaid_power = 2
    initial_water = 16
    evaporated_water = 4
    remaining_water = initial_water - evaporated_water
    total_water = remaining_water * 4
    total_liquid = total_water + koolaid_power
    percentage_koolaid = (koolaid_power / total_liquid) * 100
    result = percentage_koolaid
    return result

print(solution())