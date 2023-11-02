def solution():
    """A pastry chef is making brownies but is running out of butter. The recipe he is following calls for 2 ounces of butter for every 1 cup of baking mix; however, it allows 2 ounces of coconut oil to be substituted for the 2 ounces of butter if necessary. The chef would like to use as much butter as possible before switching over and substituting coconut oil. If the chef had 4 ounces of butter remaining, and he plans on using 6 cups of baking mix, how many ounces of coconut oil will he end up using?"""
    butter_needed = 2 * 6  # 2 ounces of butter per 1 cup of baking mix, and 6 cups of baking mix needed
    butter_remaining = 4
    if butter_remaining >= butter_needed:  # using all the butter
        coconut_oil_used = 0
    else:  # substituting with coconut oil
        coconut_oil_needed = butter_needed - butter_remaining
        coconut_oil_used = coconut_oil_needed / 2  # 2 ounces of coconut oil for every 2 ounces of butter substituted
    result = coconut_oil_used
    return result

print(solution())