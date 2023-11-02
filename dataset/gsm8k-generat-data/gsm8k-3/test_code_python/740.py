def solution():
    """Angie bought three times as many pretzels at the mall as Shelly did. Shelly bought half as many pretzels as Barry. If Barry bought 12 pretzels, how many did Angie buy?"""
    # Define the number of pretzels Barry bought
    barry_pretzels = 12

    # Calculate the number of pretzels Shelly bought
    shelly_pretzels = barry_pretzels / 2

    # Calculate the number of pretzels Angie bought
    angie_pretzels = shelly_pretzels * 3

    # Display the number of pretzels Angie bought
    result = angie_pretzels
    return result

print(solution())