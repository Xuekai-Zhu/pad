def solution():
    """Six kids and two adults are going to the circus. Kid's tickets are on sale for only half of the adult tickets. The total cost is $50. How much is one kid's ticket?"""
    # Define the number of kids and adults
    num_kids = 6
    num_adults = 2

    # Define the cost of an adult ticket
    adult_cost = x

    # Define the cost of a kid's ticket in terms of the adult ticket price
    kid_cost = adult_cost / 2

    # Calculate the total cost of the tickets
    total_cost = (num_kids * kid_cost) + (num_adults * adult_cost)

    # Solve for the cost of an adult ticket
    solve_for_x = total_cost - (num_kids * kid_cost)
    x = (solve_for_x / num_adults)

    # Calculate the cost of a kid's ticket
    kid_ticket_cost = adult_cost / 2

    # Display the cost of a kid's ticket
    result = kid_ticket_cost
    return result

print(solution())