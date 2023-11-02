def solution():
    mangoes_picked = 54
    ripe_mangoes = mangoes_picked / 3
    unripe_mangoes = mangoes_picked - ripe_mangoes
    pickled_mangoes = unripe_mangoes - 16
    mangoes_per_jar = 4
    jars = pickled_mangoes / mangoes_per_jar
    result = jars
    return result

print(solution())