def solution():
    """Daniela goes shopping during a sale. She finds out that the store has 40 percent off on shoes and 20 percent off dresses. If Daniela buys 2 pairs of shoes originally priced at $50 a pair and a dress originally priced at $100, how much money does she spend?"""
    # Define the original prices of the shoes and dress
    shoe_price = 50
    dress_price = 100

    # Calculate the discount on shoes and dress
    shoe_discount = 0.4
    dress_discount = 0.2

    # Calculate the new prices of the shoes and dress after discount
    new_shoe_price = shoe_price - (shoe_price * shoe_discount)
    new_dress_price = dress_price - (dress_price * dress_discount)

    # Calculate the total cost of the shoes and dress
    total_cost = (new_shoe_price * 2) + new_dress_price

    result = total_cost
    return result

print(solution())