def solution():
    starting_weight = 60 # the starting weight of the vest in pounds
    increased_weight = starting_weight * 1.6 # the weight increase by 60%
    total_weight = increased_weight - starting_weight # the additional weight needed
    total_ingots = total_weight / 2 # the number of 2-pound steel ingots needed
    cost_per_ingot = 5 # the cost per ingot in dollars
    if total_ingots > 10:
        cost_per_ingot *= 0.8 # applying the discount if more than 10 ingots are bought
    total_cost = total_ingots * cost_per_ingot # the total cost for all the ingots
    result = total_cost
    return result

print(solution())