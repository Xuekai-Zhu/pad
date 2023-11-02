def solution():
    """Mary just arrived at the beach. She has 4 times as many towels as Frances does. The total weight of their towels is 60 pounds. If Mary has 24 towels, how much do Frances's towels weigh in ounces?"""
    mary_towels = 24
    frances_towels = mary_towels / 4
    total_towels = mary_towels + frances_towels
    total_weight = 60 * 16 # convert pounds to ounces
    weight_per_towel = total_weight / total_towels
    frances_weight = frances_towels * weight_per_towel
    result = frances_weight
    return result

print(solution())