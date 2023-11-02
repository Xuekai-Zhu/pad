def solution():
    # Define ticket prices
    adult_ticket = 30
    child_ticket = adult_ticket / 2

    # Calculate total cost of tickets
    num_adults = 10 - 4
    num_children = 4
    total_cost = (num_adults * adult_ticket) + (num_children * child_ticket)

    # Apply discount for bringing a soda
    discount = total_cost * 0.2
    total_cost -= discount

    # Add cost of soda
    total_cost += 5

    result = total_cost
    return result

print(solution())