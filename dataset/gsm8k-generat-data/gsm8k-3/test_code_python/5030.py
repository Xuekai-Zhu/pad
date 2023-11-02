def solution():
    """One ticket to the underground costs $3. In one minute, the metro sells an average of 5 such tickets. What will be the earnings from the tickets in 6 minutes?"""
    # Define the ticket price
    TICKET_PRICE = 3

    # Define the number of tickets sold per minute
    TICKETS_SOLD_PER_MINUTE = 5

    # Calculate the number of tickets sold in 6 minutes
    tickets_sold = 6 * TICKETS_SOLD_PER_MINUTE

    # Calculate the earnings from the tickets sold in 6 minutes
    earnings = tickets_sold * TICKET_PRICE

    # Display the earnings
    result = earnings
    return result

print(solution())