def solution():
    """Daniela goes shopping during a sale. She finds out that the store has 40 percent off on shoes and 20 percent off dresses. If Daniela buys 2 pairs of shoes originally priced at $50 a pair and a dress originally priced at $100, how much money does she spend?"""
    # Define the original prices of the shoes and dress
    SHOE_PRICE_ORIGINAL = 50
    DRESS_PRICE_ORIGINAL = 100

    # Define the discounts for shoes and dress
    SHOE_DISCOUNT = 0.4
    DRESS_DISCOUNT = 0.2

    # Calculate the prices of the shoes and dress after the discounts
    shoe_price_discounted = SHOE_PRICE_ORIGINAL * (1 - SHOE_DISCOUNT)
    dress_price_discounted = DRESS_PRICE_ORIGINAL * (1 - DRESS_DISCOUNT)

    # Calculate the total cost of the purchase
    total_cost = (2 * shoe_price_discounted) + dress_price_discounted

    # Display the total cost
    result = total_cost
    return result

print(solution())