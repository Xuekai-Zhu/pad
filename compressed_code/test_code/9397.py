def solution():
    
    soda_packs = 3
    sodas_per_pack = 12
    total_sodas = soda_packs * sodas_per_pack
    people_at_party = 6
    half_people = people_at_party / 2
    sodas_left = total_sodas - (half_people * 3) - (2 * 4) - 5
    result = sodas_left
    return result

print(solution())