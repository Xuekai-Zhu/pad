def solution():
    """John has to get a new blanket. He decides to have a 7 foot by 8-foot quilt made. The quilt costs $40 per square foot. How much does his quilt cost?"""
    length = 7
    width = 8
    cost_per_sqfoot = 40
    area = length * width
    total_cost = area * cost_per_sqfoot
    result = total_cost
    return result

print(solution())