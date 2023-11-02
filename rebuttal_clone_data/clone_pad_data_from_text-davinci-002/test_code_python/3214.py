def solution():
    total_chickens = 400
    chickens_dead = 0.4 * total_chickens
    chickens_bought = chickens_dead * 10
    result = total_chickens + chickens_bought
    return result

print(solution())