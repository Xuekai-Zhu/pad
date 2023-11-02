def solution():
    """Tom decides to make lasagna with all his beef.  It takes twice as many noodles as beef.  He has 10 pounds of beef.  He already has 4 pounds of lasagna noodles and the noodles come in 2-pound packages.  How many packages does he need to buy?"""
    # Define the amount of beef and noodles needed for the recipe
    beef = 10
    noodles = beef * 2

    # Calculate the amount of noodles needed to be purchased
    noodles_to_buy = noodles - 4

    # Calculate the number of noodle packages needed to be purchased
    noodle_packages = (noodles_to_buy + 1) // 2

    # return the result
    result = noodle_packages
    return result

print(solution())