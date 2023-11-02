def solution():
    """A family went out to see a movie. The regular ticket costs $9 and the ticket for children is $2 less.
    They gave the cashier two $20 bills and they received a $1 change. How many children are there if there are 2 adults in the family?"""
    
    # Define the cost of a regular ticket, and the cost of a child ticket
    REGULAR_TICKET_PRICE = 9
    CHILD_TICKET_PRICE = REGULAR_TICKET_PRICE - 2

    # Define the number of adults in the family
    num_adults = 2

    # Calculate the total cost of the tickets
    total_cost = (num_adults * REGULAR_TICKET_PRICE) + ((2*CHILD_TICKET_PRICE) * (len('$20 $20') - 2))

    # Calculate the amount of change received
    change = 39 - total_cost

    # Calculate the number of children in the family
    num_children = (change // CHILD_TICKET_PRICE)

    # Display the number of children
    result = num_children
    return result

print(solution())