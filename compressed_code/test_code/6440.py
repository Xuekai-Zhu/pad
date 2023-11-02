def solution():
    
    num_family_members = 8
    total_hamburger = 4
    hamburger_per_meatball = 1/8
    num_meatballs = total_hamburger / hamburger_per_meatball
    num_meatballs_per_person = num_meatballs / num_family_members
    num_meatballs_antonio = num_meatballs_per_person
    
    return num_meatballs_antonio

print(solution())