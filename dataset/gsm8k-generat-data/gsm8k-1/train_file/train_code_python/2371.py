def solution():
    """Mr. Smith takes his wife, his parents, and his 3 children to a seafood buffet. The price for the adult buffet is $30. The price for the children’s buffet is $15. Senior citizens get a 10% discount. How much does Mr. Smith spend on the buffet for his entire family?"""
    num_adults = 2    # Mr. Smith and his wife are adults
    num_seniors = 2   # Mr. Smith's parents are seniors
    num_children = 3
    adult_price = 30
    child_price = 15
    senior_discount = 0.1
    total_adults = num_adults + num_seniors   # calculate total number of adults after adding Mr. Smith's parents
    total_cost_adults = total_adults * adult_price   # calculate cost of the adult buffet for all adults
    total_cost_children = num_children * child_price   # calculate cost of the children's buffet for all children
    total_cost = total_cost_adults + total_cost_children   # calculate total cost before senior discount
    total_cost_with_discount = total_cost - (total_adults * adult_price * senior_discount)   # apply senior discount
    result = total_cost_with_discount
    return result

print(solution())