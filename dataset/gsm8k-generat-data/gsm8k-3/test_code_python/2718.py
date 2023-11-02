def solution():
    """In the Oprah Winfrey High School marching band, each trumpet and clarinet player carries 5 pounds of weight, each trombone player carries 10 pounds of weight, each tuba player carries 20 pounds of weight, and each drum player carries 15 pounds of weight. If there are 6 trumpets, 9 clarinets, 8 trombones, 3 tubas, and 2 drummers, how much weight does the total marching band carry?"""
    # Define the weight of each type of player
    TRUMPET_WEIGHT = 5
    CLARINET_WEIGHT = 5
    TROMBONE_WEIGHT = 10
    TUBA_WEIGHT = 20
    DRUM_WEIGHT = 15

    # Define the number of players of each type
    trumpet_players = 6
    clarinet_players = 9
    trombone_players = 8
    tuba_players = 3
    drum_players = 2

    # Calculate the total weight of the trumpet players
    trumpet_weight = trumpet_players * TRUMPET_WEIGHT

    # Calculate the total weight of the clarinet players
    clarinet_weight = clarinet_players * CLARINET_WEIGHT

    # Calculate the total weight of the trombone players
    trombone_weight = trombone_players * TROMBONE_WEIGHT

    # Calculate the total weight of the tuba players
    tuba_weight = tuba_players * TUBA_WEIGHT

    # Calculate the total weight of the drum players
    drum_weight = drum_players * DRUM_WEIGHT

    # Calculate the total weight of the marching band
    total_weight = trumpet_weight + clarinet_weight + trombone_weight + tuba_weight + drum_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())