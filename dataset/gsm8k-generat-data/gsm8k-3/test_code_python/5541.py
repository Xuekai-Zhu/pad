def solution():
    """Five adults and two children go to see a movie and buy $12 worth of concessions. The total cost of their trip is $76. If each child's ticket is $7, how much, in dollars, are the adult tickets?"""
    # Define the price of a child's ticket and the number of children
    CHILD_PRICE = 7
    NUM_CHILDREN = 2

    # Calculate the total cost of the children's tickets
    children_cost = CHILD_PRICE * NUM_CHILDREN

    # Calculate the total cost of the movie tickets and concessions for the adults
    adult_cost = 76 - children_cost - 12

    # Calculate the cost per adult ticket
    num_adults = 5
    adult_ticket_cost = adult_cost / num_adults

    # Display the cost per adult ticket
    result = adult_ticket_cost
    return result

print(solution())