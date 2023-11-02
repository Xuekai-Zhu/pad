def solution():
    """Marta is arranging floral centerpieces for a reception party. Each arrangement needs to have 8 roses, 12 daisies, 3 snapdragons and twice as many lilies. The reception will have 10 tables. How many flowers will she need in total to fill this order?"""
    # Define the number of flowers needed for each arrangement
    roses = 8
    daisies = 12
    snapdragons = 3
    lilies = 2 * snapdragons

    # Calculate the total number of flowers needed for all the arrangements
    flowers_per_arrangement = roses + daisies + snapdragons + lilies
    total_flowers = flowers_per_arrangement * 10

    result = total_flowers
    return result

print(solution())