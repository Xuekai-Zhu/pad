def solution():
    """John is laying the foundation for 3 homes. Each home needs a slab of concrete that is 100 feet by 100 feet by .5 feet. Concrete has a density of 150 pounds per cubic foot. A pound of concrete cost $.02 per pound. How much does the foundation cost?"""
    slab_volume = 100 * 100 * 0.5
    concrete_density = 150
    slab_weight = slab_volume * concrete_density
    concrete_cost_per_pound = 0.02
    total_cost = slab_weight * concrete_cost_per_pound * 3
    result = total_cost 
    return result

print(solution())