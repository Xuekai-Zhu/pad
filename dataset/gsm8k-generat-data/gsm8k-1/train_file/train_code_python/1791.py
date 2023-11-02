def solution():
    """Marta is arranging floral centerpieces for a reception party. Each arrangement needs to have 8 roses, 12 daisies, 3 snapdragons and twice as many lilies. The reception will have 10 tables. How many flowers will she need in total to fill this order?"""
    roses_per_arrangement = 8
    daisies_per_arrangement = 12
    snapdragons_per_arrangement = 3
    lilies_per_arrangement = 2 * snapdragons_per_arrangement
    flowers_per_arrangement = roses_per_arrangement + daisies_per_arrangement + snapdragons_per_arrangement + lilies_per_arrangement
    arrangements_per_table = 1
    total_tables = 10
    total_flowers = flowers_per_arrangement * arrangements_per_table * total_tables
    result = total_flowers
    return result

print(solution())