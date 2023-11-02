def solution():
    """George went to a movie theater to see a movie. He paid $16 for the ticket and decided to buy some nachos. The nachos were half the price of the ticket. How much did George pay in total for the visit to the movie theater?"""
    # Define the cost of the movie ticket
    ticket_price = 16

    # Calculate the cost of the nachos
    nachos_price = ticket_price / 2

    # Calculate the total cost of the visit
    total_cost = ticket_price + nachos_price

    # Return the result
    result = total_cost
    return result

print(solution())