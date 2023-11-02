def solution():
    """Jordan picked 54 mangoes from his tree. One-third of the mangoes were ripe while the other two-thirds were not yet ripe. Jordan kept 16 unripe mangoes and gave the remainder to his sister who pickled them in glass jars. If it takes 4 mangoes to fill a jar, how many jars of pickled mangoes can Jordan's sister make?"""
    # Calculate the number of ripe mangoes
    ripe_mangoes = 54 // 3

    # Calculate the number of unripe mangoes
    unripe_mangoes = 54 - ripe_mangoes

    # Calculate the number of mangoes given to Jordan's sister
    mangoes_given = unripe_mangoes - 16

    # Calculate the number of jars that can be filled
    jars = mangoes_given // 4

    # Display the number of jars
    result = jars
    return result

print(solution())