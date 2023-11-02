def solution():
    num_family_members = 8
    num_pounds_hamburger = 4
    hamburger_per_meatball = 1/8

    # Calculate the total number of meatballs made with the 4 pounds of hamburger
    total_meatballs = num_pounds_hamburger / hamburger_per_meatball

    # Calculate the number of meatballs each family member will eat (including Antonio)
    meatballs_per_person = total_meatballs / num_family_members

    # Calculate the number of meatballs Antonio will eat
    antonios_meatballs = meatballs_per_person
    result = antonios_meatballs
    return result

print(solution())