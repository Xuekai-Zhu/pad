def solution():
    """Mary goes with her 3 children to the circus. Tickets cost $2 for adults and $1 for children. Mary pays with a $20 bill. How much change will she receive?"""
    # Define the ticket prices
    ADULT_PRICE = 2
    CHILD_PRICE = 1

    # Define the number of adults and children
    num_adults = 1
    num_children = 3

    # Calculate the total cost of the tickets
    total_cost = num_adults * ADULT_PRICE + num_children * CHILD_PRICE

    # Calculate the change Mary will receive
    change = 20 - total_cost

    # Display the change
    result = change
    return result

print(solution())