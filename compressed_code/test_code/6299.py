def solution():
    
    total_mangoes = 400
    ripe_mangoes = (3/5) * total_mangoes
    eaten_mangoes = 0.6 * ripe_mangoes
    remaining_mangoes = ripe_mangoes - eaten_mangoes
    result = remaining_mangoes
    return result

print(solution())