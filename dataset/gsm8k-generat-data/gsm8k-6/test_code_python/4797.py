def solution():
    # Calculate the total cost of soda and pizza for Zoe and her family
    num_people = 6  # Zoe and her 5 family members
    soda_cost = 0.5 * num_people  # Each bottle of soda costs half a dollar
    pizza_cost = 1 * num_people  # Each slice of pizza costs 1 dollar
    total_cost = soda_cost + pizza_cost

    result = total_cost
    return result

print(solution())