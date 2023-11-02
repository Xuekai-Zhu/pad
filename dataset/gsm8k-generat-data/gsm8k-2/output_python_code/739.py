def solution():
    """Angie bought three times as many pretzels at the mall as Shelly did. Shelly bought half as many pretzels as Barry. If Barry bought 12 pretzels, how many did Angie buy?"""
    barry_pretzels = 12
    shelly_pretzels = barry_pretzels / 2
    angie_pretzels = 3 * shelly_pretzels
    result = angie_pretzels
    return result

print(solution())