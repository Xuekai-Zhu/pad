def solution():
    """Jeremie wants to go to an amusement park with 3 friends at the end of summer. Tickets are $18 for children and a set of snack cost $5. How much will it cost Jeremie and her 3 friends to go to the amusement park and buy each of them a set of snacks?"""
    # Define the cost of a ticket and a set of snacks
    TICKET_PRICE = 18
    SNACK_PRICE = 5

    # Define the number of people going to the amusement park
    num_people = 4

    # Calculate the total cost of tickets
    ticket_cost = TICKET_PRICE * num_people

    # Calculate the total cost of snacks
    snack_cost = SNACK_PRICE * num_people

    # Calculate the total cost
    total_cost = ticket_cost + snack_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())