def solution():
    # Define the number of children and adults
    num_children = 3
    num_adults = 1

    # Calculate the total cost of the tickets
    total_cost = (num_children * 1) + (num_adults * 2)

    # Calculate the change
    change = 20 - total_cost
    result = change
    return result

print(solution())