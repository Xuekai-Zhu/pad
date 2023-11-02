def solution():
    # Calculate the total number of meatballs Antonio can make
    total_meatballs = 4 / (1/8)  # 1/8 pound of hamburger per meatball

    # Calculate the number of meatballs each family member can eat
    num_people = 8  # Antonio has 8 family members total
    num_people_eating = num_people - 1  # Antonio doesn't count himself
    meatballs_per_person = total_meatballs / num_people_eating

    # Calculate the number of meatballs Antonio will eat
    antonio_eats = meatballs_per_person

    result = antonio_eats
    return result

print(solution())