def solution():
    """Mr. Smith takes his wife, his parents, and his 3 children to a seafood buffet. The price for the adult buffet is $30. The price for the children’s buffet is $15. Senior citizens get a 10% discount. How much does Mr. Smith spend on the buffet for his entire family?"""
    num_adults = 5  # Mr. Smith, his wife, and his parents
    num_children = 3
    adult_price = 30
    child_price = 15
    senior_discount = 0.10

    # calculate total cost for adults
    total_adult_cost = num_adults * adult_price
    total_senior_discount = total_adult_cost * senior_discount
    total_adult_cost -= total_senior_discount

    # calculate total cost for children
    total_child_cost = num_children * child_price

    # calculate total cost for entire family
    total_cost = total_adult_cost + total_child_cost
    result = total_cost
    return result

print(solution())