def solution():
    # Calculate the number of Doritos bags
    doritos_bags = 80/4  # one quarter of the bags of chips are Doritos

    # Calculate the number of Doritos bags in each pile
    bags_per_pile = doritos_bags/4  # split the bags of Doritos into 4 equal piles

    result = bags_per_pile
    return result

print(solution())