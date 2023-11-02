def solution():
    """Martha is making centerpieces for her Thanksgiving dinner. There are six centerpieces, and each centerpiece uses 8 roses, twice as many orchids as roses, and a certain number of lilies. If Martha wants to spend $2700 total, and each flower costs $15, how many lilies will she put in each centerpiece?"""
    # Define the cost of each flower
    FLOWER_COST = 15

    # Define the number of centerpieces
    centerpieces = 6

    # Define the number of roses per centerpiece
    roses = 8

    # Define the ratio of orchids to roses
    orchid_ratio = 2

    # Calculate the number of orchids per centerpiece
    orchids = roses * orchid_ratio

    # Calculate the total number of flowers per centerpiece
    total_flowers = roses + orchids + x  # x is the number of lilies

    # Calculate the total cost of all the flowers
    total_cost = centerpieces * total_flowers * FLOWER_COST

    # Calculate the number of lilies per centerpiece
    x = (2700 - total_cost) / (centerpieces * FLOWER_COST) - (roses + orchids)

    # Display the number of lilies per centerpiece
    result = x
    return result

print(solution())