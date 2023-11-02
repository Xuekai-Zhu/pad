def solution():
    """Jim buys a wedding ring for $10,000. He gets his wife a ring that is twice that much and sells the first one for half its value. How much is he out of pocket?"""
    # Define the cost of Jim's wedding ring
    jim_ring = 10000

    # Calculate the cost of his wife's ring
    wife_ring = jim_ring * 2

    # Calculate the sale price of Jim's ring
    sale_price = jim_ring * 0.5

    # Calculate the total amount Jim is out of pocket
    total_cost = jim_ring + wife_ring - sale_price

    # return the result
    result = total_cost
    return result

print(solution())