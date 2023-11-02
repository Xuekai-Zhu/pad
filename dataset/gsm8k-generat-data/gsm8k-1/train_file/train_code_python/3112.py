def solution():
    """Jordan picked 54 mangoes from his tree. One-third of the mangoes were ripe while the other two-thirds were not yet ripe. Jordan kept 16 unripe mangoes and gave the remainder to his sister who pickled them in glass jars. If it takes 4 mangoes to fill a jar, how many jars of pickled mangoes can Jordan's sister make?"""
    total_mangoes = 54
    ripe_mangoes = total_mangoes/3
    unripe_mangoes = (2/3)*total_mangoes
    unripe_mangoes_kept = 16
    ripe_mangoes_given = ripe_mangoes
    unripe_mangoes_given = unripe_mangoes - unripe_mangoes_kept
    total_mangoes_given = ripe_mangoes_given + unripe_mangoes_given
    jars = total_mangoes_given/4
    result = jars
    return result

print(solution())