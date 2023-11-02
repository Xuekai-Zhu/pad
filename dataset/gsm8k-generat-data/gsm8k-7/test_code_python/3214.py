def solution():
    initial_chickens = 400
    percent_dead = 0.4
    chickens_lost = initial_chickens * percent_dead
    chickens_alive = initial_chickens - chickens_lost

    chickens_bought = 10 * chickens_lost
    total_chickens = chickens_alive + chickens_bought

    result = total_chickens
    return result

print(solution())