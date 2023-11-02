def solution():
    
    initial_tank = 4000
    transferred_tank = initial_tank * 0.75
    total_oil = transferred_tank + 3000
    half_tanker = 20000 / 2
    additional_liters = half_tanker - total_oil
    result = additional_liters
    return result

print(solution())