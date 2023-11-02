def solution():
    """Mary just arrived at the beach. She has 4 times as many towels as Frances does. The total weight of their towels is 60 pounds. If Mary has 24 towels, how much do Frances's towels weigh in ounces?"""
    mary_towels = 24
    mary_weight = (1/4) * mary_towels
    frances_towels = mary_towels / 4
    total_weight = 60 * 16  # convert pounds to ounces
    frances_weight = total_weight - (mary_weight + (frances_towels * mary_weight))
    result = frances_weight
    return result

print(solution())