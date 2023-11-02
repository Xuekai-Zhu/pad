def solution():
    total_mangoes = 400
    ripe_mangoes = total_mangoes * (3/5)
    mangoes_eaten = ripe_mangoes * (60/100)
    mangoes_remaining = ripe_mangoes - mangoes_eaten
    result = mangoes_remaining
    return result

print(solution())