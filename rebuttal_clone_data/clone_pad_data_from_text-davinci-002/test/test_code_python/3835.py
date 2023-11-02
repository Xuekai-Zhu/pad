def solution():
    donuts_bought = 4
    donuts_per_box = 12
    donuts_given_away = 18
    donuts_left = donuts_bought * donuts_per_box - donuts_given_away
    result = donuts_left
    return result

print(solution())