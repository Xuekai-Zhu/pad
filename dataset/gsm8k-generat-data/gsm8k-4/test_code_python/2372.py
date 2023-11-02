def solution():
    """Mr. Smith takes his wife, his parents, and his 3 children to a seafood buffet.  The price for the adult buffet is $30.  The price for the children’s buffet is $15.  Senior citizens get a 10% discount.  How much does Mr. Smith spend on the buffet for his entire family?"""
    # Define the number of people in Mr. Smith's family
    num_adults = 2
    num_seniors = 2
    num_children = 3

    # Define the price of adult and children buffets
    adult_price = 30
    children_price = 15

    # Calculate the total cost of adult buffets
    adult_cost = (num_adults - num_seniors) * adult_price + num_seniors * (adult_price * 0.9)

    # Calculate the total cost of children buffets
    children_cost = num_children * children_price

    # Calculate the total cost of the buffet for Mr. Smith's family
    total_cost = adult_cost + children_cost

    # return the result
    result = total_cost
    return result

print(solution())