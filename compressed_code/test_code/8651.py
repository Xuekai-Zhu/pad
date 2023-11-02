def solution():
    
    mpg = 3
    current_gas = 12
    distance_to_drive = 90
    gas_needed = (distance_to_drive / mpg) - current_gas
    result = gas_needed
    return result

print(solution())