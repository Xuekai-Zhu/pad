def solution():
    """Ashley and her family went to the movies on Saturday. Children’s tickets cost $4.25 and adult tickets cost $3.25 more. They were given a $2 discount for buying more than 3 tickets. How much did they spend if they bought two adult tickets and four children’s tickets?"""
    # Define the prices of children's and adult tickets
    CHILD_TICKET_PRICE = 4.25
    ADULT_TICKET_PRICE = CHILD_TICKET_PRICE + 3.25

    # Define the number of children and adult tickets purchased
    num_children_tickets = 4
    num_adult_tickets = 2

    # Calculate the total cost of the children's tickets
    children_total_cost = num_children_tickets * CHILD_TICKET_PRICE

    # Calculate the total cost of the adult tickets
    adult_total_cost = num_adult_tickets * ADULT_TICKET_PRICE

    # Calculate the total cost before discount
    total_cost_before_discount = children_total_cost + adult_total_cost

    # Apply the discount if eligible
    if num_children_tickets + num_adult_tickets > 3:
        total_cost_after_discount = total_cost_before_discount - 2
    else:
        total_cost_after_discount = total_cost_before_discount

    # return the result
    result = total_cost_after_discount
    return result

print(solution())