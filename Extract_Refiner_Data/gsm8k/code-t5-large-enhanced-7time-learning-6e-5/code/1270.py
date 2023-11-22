def solution():
    
    # Define the cost of an adult ticket and a child ticket
    ADULT_TICKET_COST = 12
    CHILD_TICKET_COST = 8

    # Define the cost of two popcorns
    POPCORN_COST = 3

    # Define the number of popcorns
    NUM_POPCORNS = 2

    # Calculate the total cost of the popcorns
    total_popcorn_cost = POPCORN_COST * NUM_POPCORNS

    # Calculate the total cost of everything
    total_cost = ADULT_TICKET_COST + CHILD_TICKET_COST + total_popcorn_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())