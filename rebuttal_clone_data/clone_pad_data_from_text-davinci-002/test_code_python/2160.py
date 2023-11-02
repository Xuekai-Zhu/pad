def solution():
    percent_increase = 60
    pants_cost = 50
    shirt_cost = pants_cost + (pants_cost * (percent_increase / 100))
    outfit_cost = pants_cost + shirt_cost
    result = outfit_cost
    return result

print(solution())