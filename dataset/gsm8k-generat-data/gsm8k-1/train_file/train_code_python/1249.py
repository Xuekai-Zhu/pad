def solution():
    """Lucia is a dancer. She takes 2 hip-hop classes a week, 2 ballet classes a week, and 1 jazz class a week. One hip-hop class costs $10. One ballet class costs $12, and one jazz class costs $8. What is the total cost of Lucia’s dance classes in one week?"""
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