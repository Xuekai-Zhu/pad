def solution():
    """The school band is going to a competition. Five members play the flute. There are three times as many members who play the trumpet. There are eight fewer trombone players than trumpeters, and eleven more drummers than trombone players. There are twice as many members that play the clarinet as members that play the flute. Three more members play the French horn than play the trombone. How many seats are needed on the bus?"""
    flute_players = 5
    trumpet_players = 3 * flute_players
    trombone_players = trumpet_players - 8
    drum_players = trombone_players + 11
    clarinet_players = 2 * flute_players
    frenchhorn_players = trombone_players + 3
    total_players = flute_players + trumpet_players + trombone_players + drum_players + clarinet_players + frenchhorn_players
    result = total_players
    return result

print(solution())