def solution():
    # Calculate the total cost of the Wendy's order
    total_cost = 10 + 5*5 + 4*2.5 + 5*2  # cost of Taco Salad + cost of hamburgers + cost of french fries + cost of peach lemonade

    # Calculate the cost each person should pay
    cost_per_person = total_cost / 5

    result = cost_per_person
    return result

print(solution())