def solution():
    """Jeremie wants to go to an amusement park with 3 friends at the end of summer. Tickets are $18 for children and a set of snack cost $5. How much will it cost Jeremie and her 3 friends to go to the amusement park and buy each of them a set of snacks?"""
    # Define the number of children going to the park
    num_children = 4

    # Calculate the total cost of tickets
    ticket_cost = num_children * 18

    # Calculate the cost of snacks
    snack_cost = num_children * 5

    # Calculate the total cost
    total_cost = ticket_cost + snack_cost

    result = total_cost
    return result

print(solution())