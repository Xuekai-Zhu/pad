def solution():
    """Mr. Doré bought $140 worth of pants, a $43 shirt and a $15 tie. He pays with a $200 bill. How much will the saleswoman give him back?"""
    # Define the total cost of the purchase
    total_cost = 140 + 43 + 15

    # Define the amount paid by the customer
    amount_paid = 200

    # Calculate the amount to be given back
    amount_back = amount_paid - total_cost

    result = amount_back
    return result

print(solution())