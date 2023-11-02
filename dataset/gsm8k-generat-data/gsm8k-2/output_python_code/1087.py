def solution():
    """We the People has 17 cows. Happy Good Healthy Family has two more than three times the number of cows We the People has. If their cows are taken to a ranch to graze together, how many cows will be in the ranch altogether?"""
    we_the_people_cows = 17
    happy_family_cows = 2 + 3 * we_the_people_cows
    total_cows = we_the_people_cows + happy_family_cows
    result = total_cows
    return result

print(solution())