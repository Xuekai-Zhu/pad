def solution():
    olives_needed = 80  # Clive needs 80 olives
    budget = 10  # Clive has $10 to spend
    olives_per_jar = 20  # Each jar contains 20 olives
    cost_per_jar = 1.5  # Each jar costs $1.50

    # Calculate the number of jars Clive needs to buy
    jars_needed = olives_needed / olives_per_jar

    # Calculate the total cost of the jars
    total_cost = jars_needed * cost_per_jar

    # Calculate the change Clive will have
    change = budget - total_cost
    result = change
    return result

print(solution())