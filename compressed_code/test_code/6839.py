def solution():
    
    copper_meters = 10
    plastic_meters = copper_meters + 5
    cost_per_meter = 4
    total_cost = (copper_meters + plastic_meters) * cost_per_meter
    result = total_cost
    return result

print(solution())