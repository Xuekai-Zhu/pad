def solution():
    """Tina buys 3 12-packs of soda for a party. Including Tina, 6 people are at the party. Half of the people at the party have 3 sodas each, 2 of the people have 4 and 1 person has 5. How many sodas are left over when the party is over?"""
    soda_packs = 3
    sodas_per_pack = 12
    total_sodas = soda_packs * sodas_per_pack
    people_at_party = 6
    half_people = people_at_party / 2
    sodas_left = total_sodas - (half_people * 3) - (2 * 4) - 5
    result = sodas_left
    return result

print(solution())