def solution():
    
    num_soda_packs = 3
    sodas_per_pack = 12
    total_sodas = num_soda_packs * sodas_per_pack
    num_people = 6
    half_num_people = num_people // 2

    
    sodas_consumed = half_num_people * 3 + 2 * 4 + 5
    sodas_left_over = total_sodas - sodas_consumed
    result = sodas_left_over
    return result

print(solution())