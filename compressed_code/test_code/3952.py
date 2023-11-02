def solution():
    
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