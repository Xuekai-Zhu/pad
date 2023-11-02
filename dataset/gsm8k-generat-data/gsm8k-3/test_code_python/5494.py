def solution():
    """A movie ticket for an adult costs $8, and a child's ticket costs $3. One adult is taking a group of children to the movies. She has $35. How many children can she take with her to the movies?"""
    # Define the cost of an adult ticket and a child ticket
    ADULT_TICKET_PRICE = 8
    CHILD_TICKET_PRICE = 3

    # Define the amount of money the adult has to spend
    BUDGET = 35

    # Calculate the maximum number of children the adult can take within the budget
    max_children = (BUDGET - ADULT_TICKET_PRICE) // CHILD_TICKET_PRICE

    # Display the maximum number of children the adult can take
    result = max_children
    return result

print(solution())