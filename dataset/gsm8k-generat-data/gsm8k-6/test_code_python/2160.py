def solution():
    pants_cost = 50
    shirt_cost = 1.6 * pants_cost  # John's shirt cost 60% more than his pants
    outfit_cost = pants_cost + shirt_cost  # total cost of John's outfit
    result = outfit_cost
    return result

print(solution())