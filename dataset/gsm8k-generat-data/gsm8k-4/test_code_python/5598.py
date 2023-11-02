def solution():
    """Mary just arrived at the beach. She has 4 times as many towels as Frances does. The total weight of their towels is 60 pounds. If Mary has 24 towels, how much do Frances's towels weigh in ounces?"""
    # Define the number of towels Mary has
    mary_towels = 24

    # Define the total weight of the towels
    total_weight = 60

    # Calculate the weight of one towel
    towel_weight = total_weight / (mary_towels + mary_towels/4)

    # Calculate the number of towels Frances has
    frances_towels = mary_towels / 4

    # Calculate the total weight of Frances's towels in ounces
    frances_weight = frances_towels * towel_weight * 16

    result = frances_weight
    return result

print(solution())