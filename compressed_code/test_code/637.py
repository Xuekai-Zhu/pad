def solution():
    
    total_hamburger = 4
    hamburger_per_meatball = 1/8
    total_meatballs = total_hamburger / hamburger_per_meatball
    family_members = 8
    meatballs_per_person = total_meatballs / family_members
    antonio_meatballs = meatballs_per_person
    result = antonio_meatballs
    return result

print(solution())