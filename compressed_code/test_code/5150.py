def solution():
    
    starting_gas = 10
    store_gas = 6
    doctor_gas = 2
    max_gas = 12
    remaining_gas = max_gas - (starting_gas - store_gas - doctor_gas)
    result = remaining_gas
    return result

print(solution())