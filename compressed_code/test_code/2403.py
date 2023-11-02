def solution():
    
    total_distance = 560 
    gas_capacity = 8
    gas_consumption = 8 
    refills = total_distance // 40 // (gas_capacity // gas_consumption)
    result = refills
    return result

print(solution())