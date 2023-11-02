def solution():
    # Calculate the total cost of admission for the group
    adult_tickets = 10 - 4  # number of adult tickets purchased
    total_cost = adult_tickets * 30 + 4 * 15  # cost of adult tickets plus half price for children's tickets

    # Apply the discount for bringing a soda
    total_cost *= 0.8

    # Add the cost of the soda
    total_cost += 5

    result = total_cost
    return result

print(solution())