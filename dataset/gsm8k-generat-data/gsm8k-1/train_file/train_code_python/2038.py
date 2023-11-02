def solution():
    """Leo had 400 marbles in a jar. He packed the marbles with ten marbles in each pack, and he gave some of them to his two friends, Manny and Neil. He gave Manny 1/4 of the number of packs of marbles, Neil received 1/8 of the number of packs of marbles, and he kept the rest. How many packs of marbles did Leo keep?"""
    total_marbles = 400
    marbles_per_pack = 10
    
    packs_given_away = (1/4 + 1/8) * (total_marbles / marbles_per_pack)
    packs_kept = total_marbles / marbles_per_pack - packs_given_away
    
    result = packs_kept
    return result

print(solution())