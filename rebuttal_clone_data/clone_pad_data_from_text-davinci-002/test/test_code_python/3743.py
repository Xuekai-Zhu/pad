def solution():
    t_shirts_bought = 6
    t_shirt_cost = 20
    percent_off = 50
    total_cost = t_shirts_bought * t_shirt_cost * (1 - (percent_off / 100))
    result = total_cost
    return result

print(solution())