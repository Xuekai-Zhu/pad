def solution():
    """Antonio is preparing a meal of spaghetti and meatballs for his family. His recipe for meatballs calls for 1/8 of a pound of hamburger per meatball. Antonio has 8 family members, including himself. If he uses 4 pounds of hamburger to make meatballs, and each member of the family eats an equal number of meatballs, how many meatballs will Antonio eat?"""
    num_family_members = 8
    total_hamburger = 4
    hamburger_per_meatball = 1/8
    num_meatballs = total_hamburger / hamburger_per_meatball
    num_meatballs_per_person = num_meatballs / num_family_members
    num_meatballs_antonio = num_meatballs_per_person
    
    return num_meatballs_antonio

print(solution())