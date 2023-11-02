def solution():
    """400 adults and 200 children go to a Broadway show. The price of an adult ticket is twice that of a child's ticket. What is the price of an adult ticket if the total amount collected is $16,000?"""
    # Define the number of adults and children
    num_adults = 400
    num_children = 200

    # Define the price of a child's ticket
    child_price = 1

    # Calculate the total amount collected
    total_collected = 16000

    # Calculate the total amount collected from children's tickets
    children_collected = num_children * child_price

    # Calculate the total amount collected from adult's tickets
    adults_collected = total_collected - children_collected

    # Calculate the price of an adult's ticket
    adult_price = adults_collected / (2 * num_adults)

    result = adult_price
    return result

print(solution())