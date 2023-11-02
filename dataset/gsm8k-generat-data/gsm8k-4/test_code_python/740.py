def solution():
    """Angie bought three times as many pretzels at the mall as Shelly did. Shelly bought half as many pretzels as Barry. If Barry bought 12 pretzels, how many did Angie buy?"""
    # Define the initial number of pretzels bought by Barry
    barry_pretzels = 12

    # Calculate the number of pretzels bought by Shelly
    shelly_pretzels = barry_pretzels / 2

    # Calculate the number of pretzels bought by Angie
    angie_pretzels = shelly_pretzels * 3

    # Return the result
    result = angie_pretzels
    return result

print(solution())