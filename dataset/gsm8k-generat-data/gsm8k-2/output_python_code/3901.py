def solution():
    """A pastry chef is making brownies but is running out of butter. The recipe he is following calls for 2 ounces of butter for every 1 cup of baking mix; however, it allows 2 ounces of coconut oil to be substituted for the 2 ounces of butter if necessary. The chef would like to use as much butter as possible before switching over and substituting coconut oil. If the chef had 4 ounces of butter remaining, and he plans on using 6 cups of baking mix, how many ounces of coconut oil will he end up using?"""
    butter_needed = 2 * 6  # 12 ounces of butter needed for 6 cups of baking mix
    butter_remaining = 4
    coconut_oil_needed = max(0, butter_needed - butter_remaining) / 2
    result = coconut_oil_needed
    return result

print(solution())