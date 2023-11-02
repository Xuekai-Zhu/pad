def solution():
    """A family is going to the amusement park. The adult tickets cost $22 for admission, and the tickets for children cost $7. The family consists of 2 adults and 2 children. What is the total price the family will pay for admission?"""
    # Define the prices of adult and child tickets
    adult_ticket_price = 22
    child_ticket_price = 7

    # Define the number of adults and children in the family
    num_adults = 2
    num_children = 2

    # Calculate the total cost of tickets for the family
    total_cost = (adult_ticket_price * num_adults) + (child_ticket_price * num_children)

    result = total_cost
    return result

print(solution())