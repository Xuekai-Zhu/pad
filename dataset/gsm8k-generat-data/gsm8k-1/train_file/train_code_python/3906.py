def solution():
    """Melany has to fence a 5000 feet square field with wire mesh. If one foot of wire mesh is sold at $30, and she had $120000, how many feet of the field will not be fenced?"""
    field_area = 5000**2
    cost_per_foot = 30
    total_cost = 120000
    feet_fenced = total_cost / cost_per_foot
    feet_not_fenced = field_area - feet_fenced
    result = feet_not_fenced
    return result

print(solution())