def solution():
    """Cecelia went to the milk store and found out that a gallon jar costs $2 more than a half-gallon jar. 
    If a gallon jar costs $5, calculate the total amount of money she spent on 10-gallon jars and 16 half-gallon jars."""
    cost_of_gallon_jar = 5
    cost_of_half_gallon_jar = cost_of_gallon_jar - 2
    total_cost_of_gallon_jars = 10 * cost_of_gallon_jar
    total_cost_of_half_gallon_jars = 16 * cost_of_half_gallon_jar
    total_cost = total_cost_of_gallon_jars + total_cost_of_half_gallon_jars
    result = total_cost
    return result

print(solution())