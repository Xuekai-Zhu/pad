def solution():
    sandwich_cost = 5  # Each sandwich costs $5
    num_sandwiches = 3  # Jack orders 3 sandwiches
    total_cost = sandwich_cost * num_sandwiches  # Calculate the total cost

    # Calculate the change Jack gets back from a $20 bill
    change = 20 - total_cost
    result = change
    return result

print(solution())