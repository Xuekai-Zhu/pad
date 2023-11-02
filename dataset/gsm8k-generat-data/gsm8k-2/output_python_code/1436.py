def solution():
    """Mark constructed a deck that was 30 feet by 40 feet. It cost $3 per square foot. He then paid an extra $1 per square foot for sealant. How much did he pay?"""
    width = 30
    length = 40
    area = width * length
    cost_per_sq_foot = 3
    sealant_cost_per_sq_foot = 1
    total_cost = area * (cost_per_sq_foot + sealant_cost_per_sq_foot)
    result = total_cost
    return result

print(solution())