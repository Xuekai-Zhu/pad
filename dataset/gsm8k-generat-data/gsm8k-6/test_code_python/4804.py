def solution():
    # Calculate the initial cost of one pencil and one cucumber
    initial_cost = 20  # both items cost $20 initially
    cost_pencil = initial_cost * (1 - 0.20)  # apply 20% discount on pencils
    cost_cucumber = initial_cost

    # Find the number of pencils Isabela bought
    pencils = 100 / 2  # Isabela bought twice as many cucumbers as pencils

    # Calculate the total cost of the items
    total_cost = (pencils * cost_pencil) + (100 * cost_cucumber)
    result = total_cost
    return result

print(solution())