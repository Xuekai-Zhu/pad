def solution():
    """Movie tickets cost $5 each on a Monday, twice as much on a Wednesday, and five times as much as Monday on a Saturday. If Glenn goes to the movie theater on Wednesday and Saturday, how much does he spend?"""
    # Define the ticket prices
    monday_price = 5
    wednesday_price = 2 * monday_price
    saturday_price = 5 * monday_price

    # Calculate Glenn's total cost for going to the movies
    total_cost = wednesday_price + saturday_price

    result = total_cost
    return result

print(solution())