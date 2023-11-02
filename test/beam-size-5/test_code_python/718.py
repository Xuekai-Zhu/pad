def solution():
    
    damage = 450
    unauthorized_road_maintenance = 120
    asphalt_cost = 25
    buckets_of_asphalt = 3
    total_cost = unauthorized_road_maintenance + (buckets_of_asphalt * asphalt_cost)
    savings = total_cost - damage
    result = savings
    return result

print(solution())