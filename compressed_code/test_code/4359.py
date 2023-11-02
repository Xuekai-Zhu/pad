def solution():
    
    total_gas = 16
    gas_per_mile = 1/20
    distance_to_college = 220
    gas_used_to_college = distance_to_college * gas_per_mile
    gas_left = total_gas - gas_used_to_college
    remaining_distance = gas_left * 20
    result = remaining_distance
    return result

print(solution())