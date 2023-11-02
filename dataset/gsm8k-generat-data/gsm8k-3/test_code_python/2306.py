def solution():
    """Ashley and her family went to the movies on Saturday. Children’s tickets cost $4.25 and adult tickets cost $3.25 more. They were given a $2 discount for buying more than 3 tickets. How much did they spend if they bought two adult tickets and four children’s tickets?"""
    # Define the price of a child's ticket and the additional cost of an adult ticket
    CHILD_TICKET_PRICE = 4.25
    ADULT_TICKET_ADDITIONAL_COST = 3.25

    # Define the number of children's tickets and adult tickets purchased
    num_children_tickets = 4
    num_adult_tickets = 2

    # Calculate the cost of the children's tickets
    children_cost = num_children_tickets * CHILD_TICKET_PRICE

    # Calculate the cost of the adult tickets
    adult_cost = (num_adult_tickets * (CHILD_TICKET_PRICE + ADULT_TICKET_ADDITIONAL_COST))

    # Calculate the total cost
    total_cost = children_cost + adult_cost

    # Apply discount if more than 3 tickets purchased
    if num_children_tickets + num_adult_tickets > 3:
        total_cost -= 2

    # Display the total cost
    result = total_cost
    return result

print(solution())