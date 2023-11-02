def solution():
    """Sebastian bought art exhibit tickets for his parents and himself. Tickets were $44 per person. He was also charged an $18 service fee for the online transaction. What is the total amount he paid for the tickets?"""
    # Define the price of each art exhibit ticket and the service fee
    TICKET_PRICE = 44
    SERVICE_FEE = 18

    # Calculate the total cost of the tickets with the service fee
    total_cost = (TICKET_PRICE * 3) + SERVICE_FEE

    # Return the total cost
    result = total_cost
    return result

print(solution())