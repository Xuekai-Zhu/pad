def solution():
    
    hip_hop_cost_per_class = 10
    ballet_cost_per_class = 12
    jazz_cost_per_class = 8
    hip_hop_classes_per_week = 2
    ballet_classes_per_week = 2
    jazz_classes_per_week = 1
    total_cost = (hip_hop_cost_per_class * hip_hop_classes_per_week) + (ballet_cost_per_class * ballet_classes_per_week) + (jazz_cost_per_class * jazz_classes_per_week)
    result = total_cost
    return result

print(solution())