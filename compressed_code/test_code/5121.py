def solution():
    
    players = 11
    uncautioned_players = 5
    cautioned_players = players - uncautioned_players
    yellow_cards = cautioned_players
    red_cards = yellow_cards // 2
    result = red_cards
    return result

print(solution())