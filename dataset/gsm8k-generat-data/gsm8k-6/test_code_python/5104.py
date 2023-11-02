def solution():
    flute_players = 5
    trumpet_players = 3*flute_players
    trombone_players = trumpet_players - 8
    drum_players = trombone_players + 11
    clarinet_players = 2*flute_players
    french_horn_players = trombone_players + 3
    
    total_players = flute_players + trumpet_players + trombone_players + drum_players + clarinet_players + french_horn_players
    seats_needed = total_players // 4  # We assume that one bus seat is needed for every 4 players
    
    result = seats_needed
    return result

print(solution())