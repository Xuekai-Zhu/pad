def solution():
    """We the People has 17 cows. Happy Good Healthy Family has two more than three times the number of cows We the People has. 
    If their cows are taken to a ranch to graze together, how many cows will be in the ranch altogether?"""
    we_the_people = 17
    happy_family = 2 + (3 * we_the_people)
    total_cows = we_the_people + happy_family
    result = total_cows
    return result

print(solution())