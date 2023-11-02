def solution():
    """Mr. and Mrs. Boyden take their 3 children to a leisure park. They buy tickets for the whole family. The cost of an adult ticket is $6 more than the cost of a child ticket. The total cost of the 5 tickets is $77. What is the cost of an adult ticket?"""
    # Define the number of children and adults
    num_children = 3
    num_adults = 2

    # Define the cost of a child ticket
    child_cost = 0

    # Find the cost of a child ticket by incrementing the cost until the total cost is $77
    while True:
        child_cost += 1
        total_cost = (num_children * child_cost) + (num_adults * (child_cost + 6))
        if total_cost == 77:
            break
    
    # Calculate the cost of an adult ticket
    adult_cost = child_cost + 6

    # return the result
    result = adult_cost
    return result

print(solution())