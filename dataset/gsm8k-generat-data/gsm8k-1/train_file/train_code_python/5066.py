def solution():
    """John is laying the foundation for 3 homes. Each home needs a slab of concrete that is 100 feet by 100 feet by .5 feet. Concrete has a density of 150 pounds per cubic foot. A pound of concrete cost $.02 per pound. How much does the foundation cost?"""
    homes = 3
    length = 100
    width = 100
    height = .5
    density = 150
    cost_per_pound = .02
    volume = length * width * height
    total_volume = volume * homes
    total_weight = total_volume * density
    cost = total_weight * cost_per_pound
    result = cost
    return result

print(solution())