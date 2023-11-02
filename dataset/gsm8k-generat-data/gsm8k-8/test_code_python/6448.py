def solution():
    # Define the number of kids and adults
    num_kids = 6
    num_adults = 2

    # Define the cost of an adult ticket as x
    x = 2 * (50 / (num_kids + num_adults))

    # Define the cost of a kid's ticket as half of an adult ticket
    kid_ticket_cost = x / 2

    result = kid_ticket_cost
    return result

print(solution())