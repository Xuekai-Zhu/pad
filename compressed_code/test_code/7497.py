def solution():
    
    pants_cost = 50
    shirt_cost_percent_increase = 60
    shirt_cost_increase = pants_cost * (shirt_cost_percent_increase / 100)
    shirt_cost = pants_cost + shirt_cost_increase
    outfit_cost = pants_cost + shirt_cost
    result = outfit_cost
    return result

print(solution())