def solution():
    """Marcus wants to buy a new pair of shoes. He decided to pay not more than $130 for them. He found a pair for $120, on which he got a discount of 30%. How much money will he manage to save by buying these shoes and not spending the assumed maximum amount?"""
    # Define the maximum amount Marcus is willing to pay for the shoes
    max_amount = 130

    # Define the original price of the shoes
    original_price = 120

    # Calculate the discounted price of the shoes
    discounted_price = original_price * 0.7

    # Calculate the amount of money Marcus will save by buying the discounted shoes instead of paying the maximum amount
    savings = max_amount - discounted_price

    result = savings
    return result

print(solution())