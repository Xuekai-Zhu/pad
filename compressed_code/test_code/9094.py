def solution():
    
    jars = 5
    quarters_per_jar = 160
    total_quarters = jars * quarters_per_jar
    total_dollars = total_quarters * 0.25
    bike_cost = 180
    leftover_money = total_dollars - bike_cost
    result = leftover_money
    return result

print(solution())