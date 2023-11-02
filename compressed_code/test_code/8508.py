def solution():
    
    pasta_kg = 2
    pasta_price = 1.5
    beef_kg = 0.25
    beef_price_per_kg = 8
    sauce_price_per_jar = 2
    num_jars = 2
    quesadilla_price = 6
    
    pasta_cost = pasta_kg * pasta_price
    beef_cost = beef_kg * beef_price_per_kg
    sauce_cost = num_jars * sauce_price_per_jar
    total_cost = pasta_cost + beef_cost + sauce_cost + quesadilla_price
    
    result = total_cost
    return result

print(solution())