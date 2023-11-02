def solution():
    """Mohammad has 80 bags of chips. One quarter of the bags of chips are Doritos. If Mohammad wants to split the bags of Doritos into 4 equal piles, how many bags of Doritos will be in each pile?"""
    # Define the number of bags of chips and the fraction that are Doritos
    total_bags = 80
    doritos_fraction = 0.25

    # Calculate the number of bags of Doritos
    doritos_bags = total_bags * doritos_fraction

    # Calculate the number of bags in each pile
    bags_per_pile = doritos_bags / 4

    result = bags_per_pile
    return result

print(solution())