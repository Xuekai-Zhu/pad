def solution():
    """Antonio is preparing a meal of spaghetti and meatballs for his family. His recipe for meatballs calls for 1/8 of a pound of hamburger per meatball. Antonio has 8 family members, including himself. If he uses 4 pounds of hamburger to make meatballs, and each member of the family eats an equal number of meatballs, how many meatballs will Antonio eat?"""
    total_hamburger = 4
    hamburger_per_meatball = 1/8
    total_meatballs = total_hamburger / hamburger_per_meatball
    family_members = 8
    meatballs_per_person = total_meatballs / family_members
    antonio_meatballs = meatballs_per_person
    result = antonio_meatballs
    return result

print(solution())