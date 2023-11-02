def solution():
    """400 adults and 200 children go to a Broadway show. The price of an adult ticket is twice that of a child's ticket. What is the price of an adult ticket if the total amount collected is $16,000?"""
    # Define the number of adults and children
    num_adults = 400
    num_children = 200

    # Define the price of a child ticket
    child_price = x

    # Calculate the price of an adult ticket
    adult_price = 2 * child_price

    # Calculate the total amount collected
    total_collection = (num_adults * adult_price) + (num_children * child_price)

    # Solve for the child price
    x = 16000 / (400 + 200*2)
    child_price = x

    # Calculate the adult price with the new child price
    adult_price = 2 * child_price

    # Display the adult price
    result = adult_price
    return result

print(solution())