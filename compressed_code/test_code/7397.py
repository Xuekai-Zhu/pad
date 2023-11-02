def solution():
    
    total_marbles = 400
    marbles_per_pack = 10
    
    packs_given_away = (1/4 + 1/8) * (total_marbles / marbles_per_pack)
    packs_kept = total_marbles / marbles_per_pack - packs_given_away
    
    result = packs_kept
    return result

print(solution())