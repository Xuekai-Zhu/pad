def solution():
    hamburger_per_meatball = 1/8  # Antonio needs 1/8 of a pound of hamburger per meatball
    total_hamburger = 4  # Antonio is using 4 pounds of hamburger

    # Calculate the total number of meatballs
    total_meatballs = total_hamburger / hamburger_per_meatball

    # Calculate the number of meatballs per person
    meatballs_per_person = total_meatballs / 8

    # Calculate the number of meatballs Antonio will eat
    antonio_meatballs = meatballs_per_person

    result = antonio_meatballs
    return result

print(solution())