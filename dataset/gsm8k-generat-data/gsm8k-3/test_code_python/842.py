def solution():
    """Antonio is preparing a meal of spaghetti and meatballs for his family.  His recipe for meatballs calls for 1/8 of a pound of hamburger per meatball.  Antonio has 8 family members, including himself.  If he uses 4 pounds of hamburger to make meatballs, and each member of the family eats an equal number of meatballs, how many meatballs will Antonio eat?"""
    # Define the amount of hamburger per meatball
    HAMBURGER_PER_MEATBALL = 1/8

    # Define the number of family members
    family_members = 8

    # Define the amount of hamburger used to make meatballs
    hamburger_used = 4

    # Calculate the total number of meatballs
    total_meatballs = hamburger_used / HAMBURGER_PER_MEATBALL

    # Calculate the number of meatballs per family member
    meatballs_per_person = total_meatballs / family_members

    # Calculate the number of meatballs Antonio will eat
    antonio_meatballs = meatballs_per_person

    # Display the number of meatballs Antonio will eat
    result = antonio_meatballs
    return result

print(solution())