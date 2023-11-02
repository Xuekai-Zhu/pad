def solution():
    """A pastry chef is making brownies but is running out of butter. The recipe he is following calls for 2 ounces of butter for every 1 cup of baking mix; however, it allows 2 ounces of coconut oil to be substituted for the 2 ounces of butter if necessary. The chef would like to use as much butter as possible before switching over and substituting coconut oil. If the chef had 4 ounces of butter remaining, and he plans on using 6 cups of baking mix, how many ounces of coconut oil will he end up using?"""
    # Define the amount of butter and coconut oil needed per cup of baking mix
    butter_per_cup = 2
    coconut_oil_per_cup = 2

    # Define the remaining amount of butter
    butter_remaining = 4

    # Define the number of cups of baking mix
    cups_of_mix = 6

    # Initialize the total butter and coconut oil used
    total_butter_used = 0
    total_coconut_oil_used = 0

    # Loop through each cup of baking mix, using as much butter as possible before using coconut oil.
    for i in range(cups_of_mix):
        if butter_remaining >= butter_per_cup:
            butter_remaining -= butter_per_cup
            total_butter_used += butter_per_cup
        else:
            total_coconut_oil_used += coconut_oil_per_cup

    result = total_coconut_oil_used
    return result

print(solution())