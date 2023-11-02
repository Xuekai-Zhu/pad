def solution():
    """Nine of the kids in Gina's class are allergic to dairy, 6 are allergic to peanuts and 3 are allergic to both. If there are 32 kids in her class, how many aren't allergic to anything?"""
    dairy_allergy = 9
    peanut_allergy = 6
    both_allergy = 3
    total_allergy = dairy_allergy + peanut_allergy - both_allergy
    not_allergic = 32 - total_allergy
    result = not_allergic
    return result

print(solution())