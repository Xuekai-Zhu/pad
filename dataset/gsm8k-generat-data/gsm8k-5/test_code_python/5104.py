def solution():
    # Number of members playing the flute
    flute_players = 5

    # Number of members playing the trumpet
    trumpet_players = 3 * flute_players

    # Number of members playing the trombone
    trombone_players = trumpet_players - 8

    # Number of members playing the drums
    drum_players = trombone_players + 11

    # Number of members playing the clarinet
    clarinet_players = 2 * flute_players

    # Number of members playing the French horn
    french_horn_players = trombone_players + 3

    # Total number of seats needed on the bus
    total_seats = flute_players + trumpet_players + trombone_players + drum_players + clarinet_players + french_horn_players
    result = total_seats
    return result

print(solution())