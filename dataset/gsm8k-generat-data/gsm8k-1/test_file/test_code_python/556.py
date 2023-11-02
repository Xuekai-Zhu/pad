def solution():
    """A pet shop had 6 cages of rodents. 3 of the cages have 10 hamsters and the other 3 have 5 guinea pigs. How many rodents did the pet shop have in total?"""
    hamster_cages = 3
    guinea_pig_cages = 3
    hamsters_per_cage = 10
    guinea_pigs_per_cage = 5
    total_hamsters = hamster_cages * hamsters_per_cage
    total_guinea_pigs = guinea_pig_cages * guinea_pigs_per_cage
    total_rodents = total_hamsters + total_guinea_pigs
    result = total_rodents
    return result

print(solution())