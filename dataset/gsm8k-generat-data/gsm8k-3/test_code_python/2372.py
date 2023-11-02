def solution():
    """Mr. Smith takes his wife, his parents, and his 3 children to a seafood buffet.  The price for the adult buffet is $30.  The price for the children’s buffet is $15.  Senior citizens get a 10% discount.  How much does Mr. Smith spend on the buffet for his entire family?"""
    # Define the prices of the adult and children's buffets
    ADULT_PRICE = 30
    CHILD_PRICE = 15

    # Define the number of adults, children, and senior citizens
    num_adults = 3
    num_children = 3
    num_seniors = 2

    # Calculate the cost of the adult buffets
    adult_cost = num_adults * ADULT_PRICE

    # Calculate the cost of the children's buffets
    child_cost = num_children * CHILD_PRICE

    # Calculate the cost of the senior citizens' buffets
    senior_cost = num_seniors * ADULT_PRICE * 0.9

    # Calculate the total cost
    total_cost = adult_cost + child_cost + senior_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())