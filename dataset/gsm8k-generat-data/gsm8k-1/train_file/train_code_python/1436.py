def solution():
    """Mark constructed a deck that was 30 feet by 40 feet. It cost $3 per square foot. He then paid an extra $1 per square foot for sealant. How much did he pay?"""
    length = 30
    width = 40
    area = length * width
    cost_per_sqft = 3
    sealant_cost_per_sqft = 1
    total_cost = (area * cost_per_sqft) + (area * sealant_cost_per_sqft)
    result = total_cost
    return result

print(solution())