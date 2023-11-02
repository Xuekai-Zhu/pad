def solution():
    
    slab_volume = 100 * 100 * 0.5
    concrete_density = 150
    slab_weight = slab_volume * concrete_density
    concrete_cost_per_pound = 0.02
    total_cost = slab_weight * concrete_cost_per_pound * 3
    result = total_cost 
    return result

print(solution())