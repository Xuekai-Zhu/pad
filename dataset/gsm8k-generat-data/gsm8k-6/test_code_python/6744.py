def solution():
    # Calculate the cost of cherries purchased by Genevieve
    total_cost = 400 + 1600  # Genevieve was $400 short and had $1600
    cost_per_kg = 8  # cost per kilogram of cherries
    kg_of_cherries = total_cost / cost_per_kg  # calculate the number of kilograms of cherries
    result = kg_of_cherries
    return result

print(solution())