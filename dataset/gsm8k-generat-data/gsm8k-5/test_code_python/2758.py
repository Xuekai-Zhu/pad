def solution():
    num_bags = 80  # Mohammad has 80 bags of chips
    num_doritos = num_bags / 4  # One quarter of the bags are Doritos

    # Divide the bags of Doritos into 4 equal piles
    num_per_pile = num_doritos / 4
    result = num_per_pile
    return result

print(solution())