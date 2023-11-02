def solution():
    total_budget = 10
    num_olives_needed = 80
    num_olives_per_jar = 20
    jar_price = 1.5

    # Calculate the total number of jars of olives needed
    num_jars_needed = num_olives_needed / num_olives_per_jar

    # Calculate the total cost of all jars of olives needed
    total_cost = num_jars_needed * jar_price

    # Calculate the change that Clive will have
    change = total_budget - total_cost
    result = change
    return result

print(solution())