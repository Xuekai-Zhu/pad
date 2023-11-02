def solution():
    """Marcus wants to buy a new pair of shoes. He decided to pay not more than $130 for them.
    He found a pair for $120, on which he got a discount of 30%. How much money will he manage
    to save by buying these shoes and not spending the assumed maximum amount?"""
    # Define the maximum amount Marcus is willing to pay
    MAX_AMOUNT = 130

    # Define the original price of the shoes and the discount percentage
    ORIGINAL_PRICE = 120
    DISCOUNT_PERCENT = 0.3

    # Calculate the discounted price of the shoes
    discounted_price = ORIGINAL_PRICE - (ORIGINAL_PRICE * DISCOUNT_PERCENT)

    # Calculate the amount saved by buying the discounted shoes instead of paying the maximum amount
    amount_saved = MAX_AMOUNT - discounted_price

    # Display the amount saved
    result = amount_saved
    return result

print(solution())