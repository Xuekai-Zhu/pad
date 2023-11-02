def solution():
    """Amara had 100 pieces of clothing but started donating her clothes to others. She donated 5 to one orphanage home and triple that to another orphanage home. If she decides to throw away 15 of her old clothes, how many pieces of clothing does she have remaining?"""
    starting_clothes = 100
    donated_to_1st_home = 5
    donated_to_2nd_home = 3 * donated_to_1st_home
    thrown_away = 15
    remaining_clothes = starting_clothes - donated_to_1st_home - donated_to_2nd_home - thrown_away
    result = remaining_clothes
    return result

print(solution())