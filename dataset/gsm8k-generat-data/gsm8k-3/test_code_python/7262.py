def solution():
    """Sebastian bought art exhibit tickets for his parents and himself. Tickets were $44 per person. He was also charged an $18 service fee for the online transaction. What is the total amount he paid for the tickets?"""
    # Define the cost of each ticket and the service fee
    TICKET_COST = 44
    SERVICE_FEE = 18

    # Define the number of tickets purchased
    tickets_purchased = 3

    # Calculate the total cost of the tickets
    tickets_cost = TICKET_COST * tickets_purchased

    # Add the service fee to the total cost of the tickets
    total_cost = tickets_cost + SERVICE_FEE

    # Display the total cost
    result = total_cost
    return result

print(solution())