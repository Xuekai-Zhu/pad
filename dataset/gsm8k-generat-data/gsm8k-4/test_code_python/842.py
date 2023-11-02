def solution():
    """Antonio is preparing a meal of spaghetti and meatballs for his family. His recipe for meatballs calls for 1/8 of a pound of hamburger per meatball. Antonio has 8 family members, including himself. If he uses 4 pounds of hamburger to make meatballs, and each member of the family eats an equal number of meatballs, how many meatballs will Antonio eat?"""
    # Define the amount of hamburger in pounds needed per meatball
    hamburger_per_meatball = 1/8

    # Calculate the total number of meatballs that can be made with 4 pounds of hamburger
    total_meatballs = 4 / hamburger_per_meatball

    # Calculate the number of meatballs per person
    meatballs_per_person = total_meatballs / 8

    # Calculate the number of meatballs that Antonio will eat
    antonio_meatballs = meatballs_per_person * 1

    result = antonio_meatballs
    return result

print(solution())