def solution():
    """A pastry chef is making brownies but is running out of butter.  The recipe he is following calls for 2 ounces of butter for every 1 cup of baking mix; however, it allows 2 ounces of coconut oil to be substituted for the 2 ounces of butter if necessary.  The chef would like to use as much butter as possible before switching over and substituting coconut oil.  If the chef had 4 ounces of butter remaining, and he plans on using 6 cups of baking mix, how many ounces of coconut oil will he end up using?"""
    # Define the amount of butter and coconut oil needed per cup of baking mix
    BUTTER_PER_CUP = 2
    COCONUT_OIL_PER_CUP = 2

    # Define the number of cups of baking mix
    baking_mix_cups = 6

    # Define the amount of butter available
    available_butter = 4

    # Calculate the maximum amount of butter that can be used
    max_butter = min(available_butter, baking_mix_cups * BUTTER_PER_CUP)

    # Calculate the amount of coconut oil needed
    coconut_oil_needed = baking_mix_cups * COCONUT_OIL_PER_CUP - max_butter

    # Display the amount of coconut oil needed
    result = coconut_oil_needed
    return result

print(solution())