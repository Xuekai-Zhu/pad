def solution():
    """Mary just arrived at the beach. She has 4 times as many towels as Frances does. The total weight of their towels is 60 pounds. If Mary has 24 towels, how much do Frances's towels weigh in ounces?"""
    # Define the number of towels and weight per towel for Mary
    mary_towels = 24
    mary_weight_per_towel = 60 / (4 * mary_towels)

    # Define the number and weight per towel for Frances
    frances_towels = mary_towels / 4
    frances_weight_per_towel = mary_weight_per_towel

    # Calculate the total weight of Frances's towels in ounces
    total_weight_frances = frances_towels * frances_weight_per_towel * 16

    # Display the total weight of Frances's towels in ounces
    result = total_weight_frances
    return result

print(solution())