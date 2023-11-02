def solution():
    total_mangoes = 54  # Jordan picked 54 mangoes
    ripe_mangoes = total_mangoes / 3  # One-third of the mangoes were ripe
    unripe_mangoes = 2 * ripe_mangoes  # The other two-thirds were unripe
    unripe_mangoes_kept = 16  # Jordan kept 16 unripe mangoes
    unripe_mangoes_given = unripe_mangoes - unripe_mangoes_kept  # Jordan gave the remainder to his sister
    jars_filled = unripe_mangoes_given // 4  # It takes 4 mangoes to fill a jar

    result = jars_filled
    return result

print(solution())