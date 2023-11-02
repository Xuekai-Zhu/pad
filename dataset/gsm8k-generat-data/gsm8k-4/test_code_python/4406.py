def solution():
    """Collin has 25 flowers. Ingrid gives Collin a third of her 33 flowers. If each flower has 4 petals, how many petals does Collin have in total?"""
    # Define the initial number of flowers and the number of petals per flower
    collin_flowers = 25
    ingrid_flowers = 33
    petals_per_flower = 4

    # Calculate the number of flowers Collin receives from Ingrid
    ingrid_gift = ingrid_flowers / 3

    # Calculate the total number of flowers Collin has
    total_flowers = collin_flowers + ingrid_gift

    # Calculate the total number of petals Collin has
    total_petals = total_flowers * petals_per_flower

    result = total_petals
    return result

print(solution())