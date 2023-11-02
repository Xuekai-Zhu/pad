def solution():
    """Mr. and Mrs. Boyden take their 3 children to a leisure park. They buy tickets for the whole family. The cost of an adult ticket is $6 more than the cost of a child ticket. The total cost of the 5 tickets is $77. What is the cost of an adult ticket?"""
    # Define the number of children and adults
    num_children = 3
    num_adults = 2

    # Define the cost of a child ticket
    child_cost = x

    # Calculate the cost of an adult ticket
    adult_cost = child_cost + 6

    # Calculate the total cost of the tickets
    total_cost = num_children * child_cost + num_adults * adult_cost

    # Solve for x (the cost of a child ticket)
    x = (77 - 2 * adult_cost) / 3

    # Display the cost of an adult ticket
    result = adult_cost
    return result

print(solution())