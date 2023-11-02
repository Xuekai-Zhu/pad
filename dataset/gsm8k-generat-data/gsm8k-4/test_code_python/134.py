def solution():
    """A couple with two children, ages 6 and 10 years old, decided to go to an amusement park. The regular ticket costs $109, but children below 12 years old have a $5 discount. If they gave the cashier $500, how much change will they receive?"""
    # Define the cost of the regular tickets and the age of the children
    regular_ticket_cost = 109
    child_discount = 5
    child1_age = 6
    child2_age = 10

    # Calculate the cost of the tickets with children's discount
    child1_ticket_cost = regular_ticket_cost - child_discount
    child2_ticket_cost = regular_ticket_cost - child_discount

    # Calculate the total cost of the tickets
    total_cost = regular_ticket_cost + child1_ticket_cost + child2_ticket_cost

    # Calculate the change they will receive
    change = 500 - total_cost

    # Return the result
    result = change
    return result

print(solution())