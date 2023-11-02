def solution():
    """Jordan picked 54 mangoes from his tree. One-third of the mangoes were ripe while the other two-thirds were not yet ripe. Jordan kept 16 unripe mangoes and gave the remainder to his sister who pickled them in glass jars. If it takes 4 mangoes to fill a jar, how many jars of pickled mangoes can Jordan's sister make?"""
    # Define the number of mangoes picked by Jordan
    total_mangoes = 54

    # Calculate the number of ripe mangoes
    ripe_mangoes = total_mangoes / 3

    # Calculate the number of unripe mangoes Jordan kept
    unripe_mangoes = 16

    # Calculate the number of mangoes given to Jordan's sister
    sister_mangoes = total_mangoes - ripe_mangoes - unripe_mangoes

    # Calculate the number of jars of pickled mangoes
    jars = sister_mangoes // 4

    # return the result
    result = jars
    return result

print(solution())