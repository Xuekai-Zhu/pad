def solution():
    """Amara had 100 pieces of clothing but started donating her clothes to others. She donated 5 to one orphanage home and triple that to another orphanage home. If she decides to throw away 15 of her old clothes, how many pieces of clothing does she have remaining?"""
    initial_clothes = 100
    donated_orphanage_1 = 5
    donated_orphanage_2 = donated_orphanage_1 * 3
    thrown_away = 15
    remaining_clothes = initial_clothes - donated_orphanage_1 - donated_orphanage_2 - thrown_away
    result = remaining_clothes
    return result

print(solution())