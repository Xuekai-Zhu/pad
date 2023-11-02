def solution():
    
    packs = 5
    sodas_per_pack = 12
    starting_sodas = 10
    total_sodas = packs * sodas_per_pack + starting_sodas
    days = 7
    sodas_per_day = total_sodas / days
    result = sodas_per_day
    return result

print(solution())