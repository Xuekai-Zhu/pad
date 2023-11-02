def solution():
    """Tina buys 3 12-packs of soda for a party. Including Tina, 6 people are at the party. Half of the people at the party have 3 sodas each, 2 of the people have 4 and 1 person has 5. How many sodas are left over when the party is over?"""
    num_soda_packs = 3
    sodas_per_pack = 12
    total_sodas = num_soda_packs * sodas_per_pack
    num_people = 6
    half_num_people = num_people // 2

    # Calculate number of sodas consumed
    sodas_consumed = half_num_people * 3 + 2 * 4 + 5
    sodas_left_over = total_sodas - sodas_consumed
    result = sodas_left_over
    return result

print(solution())