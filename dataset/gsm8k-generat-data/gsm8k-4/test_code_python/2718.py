def solution():
    """In the Oprah Winfrey High School marching band, each trumpet and clarinet player carries 5 pounds of weight, each trombone player carries 10 pounds of weight, each tuba player carries 20 pounds of weight, and each drum player carries 15 pounds of weight. If there are 6 trumpets, 9 clarinets, 8 trombones, 3 tubas, and 2 drummers, how much weight does the total marching band carry?"""
    # Define the weight carried by each type of player
    TRUMPET_WEIGHT = 5
    CLARINET_WEIGHT = 5
    TROMBONE_WEIGHT = 10
    TUBA_WEIGHT = 20
    DRUM_WEIGHT = 15

    # Calculate the total weight carried by the trumpets and clarinets
    trumps_clar_weight = (6 + 9) * TRUMPET_WEIGHT

    # Calculate the total weight carried by the trombones
    trom_weight = 8 * TROMBONE_WEIGHT

    # Calculate the total weight carried by the tubas
    tuba_weight = 3 * TUBA_WEIGHT

    # Calculate the total weight carried by the drummers
    drum_weight = 2 * DRUM_WEIGHT

    # Calculate the total weight carried by the marching band
    total_weight = trumps_clar_weight + trom_weight + tuba_weight + drum_weight

    result = total_weight
    return result

print(solution())