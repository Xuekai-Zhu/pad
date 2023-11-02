def solution():
    family_members = 11
    people_per_tent = 2
    tents_needed = (family_members - 4) / people_per_tent
    result = tents_needed
    return result

print(solution())