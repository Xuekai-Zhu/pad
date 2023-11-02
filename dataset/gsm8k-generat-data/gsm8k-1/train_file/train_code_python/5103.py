def solution():
    """
    The school band is going to a competition. Five members play the flute. There are three times as many members who play
     the trumpet. There are eight fewer trombone players than trumpeters, and eleven more drummers than trombone players. 
     There are twice as many members that play the clarinet as members that play the flute. Three more members play the 
     French horn than play the trombone. How many seats are needed on the bus?
     """
    flute_players = 5
    trumpet_players = flute_players * 3
    trombone_players = trumpet_players - 8
    clarinet_players = flute_players * 2
    french_horn_players = trombone_players + 3
    total_players = flute_players + trumpet_players + trombone_players + drum_players + clarinet_players + french_horn_players
    seats_needed = total_players
    result = seats_needed
    return result

print(solution())