def solution():
    
    total_mangoes = 54
    ripe_mangoes = total_mangoes // 3
    unripe_mangoes = total_mangoes - ripe_mangoes - 16
    jars_of_mangoes = unripe_mangoes // 4
    result = jars_of_mangoes
    return result

print(solution())