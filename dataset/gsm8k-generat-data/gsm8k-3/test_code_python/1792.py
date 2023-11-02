def solution():
    """Marta is arranging floral centerpieces for a reception party.  Each arrangement needs to have 8 roses,12 daisies, 3 snapdragons and twice as many lilies.  The reception will have 10 tables.  How many flowers will she need in total to fill this order?"""
    # Define the number of each type of flower in each arrangement
    ROSES_PER_ARRANGEMENT = 8
    DAISIES_PER_ARRANGEMENT = 12
    SNAPDRAGONS_PER_ARRANGEMENT = 3
    LILIES_PER_ARRANGEMENT = 2 * DAISIES_PER_ARRANGEMENT

    # Define the number of tables
    NUM_TABLES = 10

    # Calculate the total number of each type of flower needed for all the arrangements
    total_roses = ROSES_PER_ARRANGEMENT * NUM_TABLES
    total_daisies = DAISIES_PER_ARRANGEMENT * NUM_TABLES
    total_snapdragons = SNAPDRAGONS_PER_ARRANGEMENT * NUM_TABLES
    total_lilies = LILIES_PER_ARRANGEMENT * NUM_TABLES

    # Calculate the total number of flowers needed
    total_flowers = total_roses + total_daisies + total_snapdragons + total_lilies

    # Display the total number of flowers needed
    result = total_flowers
    return result

print(solution())