def solution():
    """There are 320 ducks in a pond.  On the first night 1/4 of them get eaten by a fox.  On the second night 1/6 of the remaining ducks fly away, and on the third night 30 percent are stolen.  How many ducks remain after the three nights?"""
    # Total number of ducks in the pond
    total_ducks = 320

    # Number of ducks eaten by the fox on the first night
    ducks_eaten = total_ducks * 0.25

    # Number of ducks remaining after the first night
    ducks_remaining = total_ducks - ducks_eaten

    # Number of ducks that fly away on the second night
    ducks_flew_away = ducks_remaining * (1 / 6)

    # Number of ducks remaining after the second night
    ducks_left = ducks_remaining - ducks_flew_away

    # Number of ducks that are stolen on the third night
    ducks_stolen = ducks_left * 0.3

    # Number of ducks remaining after the third night
    ducks_final = ducks_left - ducks_stolen

    result = ducks_final
    return result

print(solution())