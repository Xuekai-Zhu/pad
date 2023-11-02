def solution():
    num_sandwiches = 20
    pounds_per_sandwich = 1
    pounds_per_person = 4
    cost_per_pound = 7.0
    cost_per_pound = 3.0

    # Calculate the total pounds of meat and cheese needed for all sandwiches
    total_pounds = num_sandwiches * pounds_per_sandwich

    # Calculate the total cost of meat and cheese needed for all sandwiches
    total_meat_cost = total_pounds * cost_per_pound
    total_cheese_cost = total_pounds * cost_per_pound

    # Calculate the total cost of all meat and cheese for all sandwiches
    total_cost = total_meat_cost + total_cheese_cost
    result = total_cost
    return result

print(solution())