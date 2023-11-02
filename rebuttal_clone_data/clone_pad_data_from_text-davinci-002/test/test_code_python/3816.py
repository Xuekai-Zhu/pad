def solution():
    cakes_baked = 20
    days_worked = 9
    cakes_sold = (cakes_baked * days_worked) / 2
    cakes_left = cakes_baked * days_worked - cakes_sold
    result = cakes_left
    return result

print(solution())