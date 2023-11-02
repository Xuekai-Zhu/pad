def solution():
    # Calculate the total number of wood bundles burned in the morning
    morning_burn = 4
    # Calculate the total number of wood bundles burned throughout the day
    total_burn = 10 - 3
    # Calculate the number of wood bundles burned in the afternoon
    afternoon_burn = total_burn - morning_burn
    result = afternoon_burn
    return result

print(solution())