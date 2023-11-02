def solution():
    
    pasta_cost_per_kg = 1.5
    pasta_weight = 2
    pasta_cost = pasta_cost_per_kg * pasta_weight

    beef_cost_per_kg = 8
    beef_weight = 0.25
    beef_cost = beef_cost_per_kg * beef_weight

    pasta_sauce_cost_per_jar = 2
    pasta_sauce_quantity = 2
    pasta_sauce_cost = pasta_sauce_cost_per_jar * pasta_sauce_quantity

    snacks_cost = 6

    total_cost = pasta_cost + beef_cost + pasta_sauce_cost + snacks_cost
    result = total_cost
    return result

print(solution())