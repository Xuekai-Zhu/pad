def solution():
    # Calculate the cost of each item
    broccoli_cost = 4 * 3  # $4 per pound, 3 pounds
    orange_cost = 0.75 * 3  # $0.75 per orange, 3 oranges
    cabbage_cost = 3.75  # $3.75 for one cabbage
    bacon_cost = 3  # $3 for one pound of bacon
    chicken_cost = 3 * 2  # $3 per pound, 2 pounds of chicken

    # Calculate the total cost and the cost of meat
    total_cost = broccoli_cost + orange_cost + cabbage_cost + bacon_cost + chicken_cost
    meat_cost = bacon_cost + chicken_cost

    # Calculate the percentage of the grocery budget spent on meat
    meat_percentage = int((meat_cost / total_cost) * 100 + 0.5)  # Round to the nearest percent

    result = meat_percentage
    return result

print(solution())