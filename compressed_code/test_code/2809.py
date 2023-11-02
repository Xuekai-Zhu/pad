def solution():
    
    mpg = 3
    distance = 90
    current_gas = 12
    remaining_distance = distance - (current_gas * mpg)
    additional_gas = remaining_distance / mpg
    result = additional_gas
    return result

print(solution())