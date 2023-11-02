def solution():
    """Lucia is a dancer. She takes 2 hip-hop classes a week, 2 ballet classes a week, and 1 jazz class a week. One hip-hop class costs $10. One ballet class costs $12, and one jazz class costs $8. What is the total cost of Lucia’s dance classes in one week?"""
    hip_hop_cost = 10
    ballet_cost = 12
    jazz_cost = 8
    total_cost = (2 * hip_hop_cost * 2) + (2 * ballet_cost * 2) + (1 * jazz_cost)
    result = total_cost
    return result

print(solution())