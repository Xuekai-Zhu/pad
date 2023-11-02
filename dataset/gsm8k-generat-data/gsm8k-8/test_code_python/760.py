def solution():
    # Calculate the total number of servings needed
    servings_needed = 30 * 2

    # Calculate the number of batches needed
    batches_needed = servings_needed // 4
    if servings_needed % 4 != 0:
        batches_needed += 1

    # Calculate the total cost of potatoes
    potato_cost = batches_needed * 4 * 0.1

    # Calculate the total cost of salt
    salt_cost = (batches_needed // 5) * 2
    if batches_needed % 5 != 0:
        salt_cost += 2

    # Calculate the total cost of food
    total_cost = potato_cost + salt_cost
    result = total_cost
    return result

print(solution())