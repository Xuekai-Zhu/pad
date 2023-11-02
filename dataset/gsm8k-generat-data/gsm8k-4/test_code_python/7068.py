def solution():
    """James gets 3 parking tickets. The first 2 cost $150 each and the third cost 1/3 as much as one of these. His roommate agrees to pay half the cost. How much money does he have left if he had $500 in the bank?"""
    
    # Calculate the cost of the first 2 tickets
    ticket_cost_1 = 150
    ticket_cost_2 = 150
    total_cost = ticket_cost_1 + ticket_cost_2

    # Calculate the cost of the third ticket
    ticket_cost_3 = ticket_cost_1 / 3

    # Add up the total cost of all tickets
    total_cost += ticket_cost_3

    # Calculate the amount James' roommate is paying
    roommate_payment = total_cost / 2

    # Subtract the roommate's payment from the total cost
    james_payment = total_cost - roommate_payment

    # Calculate how much money James has left after paying for the tickets
    starting_amount = 500
    remaining_amount = starting_amount - james_payment

    result = remaining_amount
    return result

print(solution())