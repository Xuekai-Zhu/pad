def solution():
    """Movie tickets cost $5 each on a Monday, twice as much on a Wednesday, and five times as much as Monday on a Saturday. If Glenn goes to the movie theater on Wednesday and Saturday, how much does he spend?"""
    # Define the ticket prices
    monday_price = 5
    wednesday_price = monday_price * 2
    saturday_price = monday_price * 5

    # Calculate the total cost of tickets for Glenn
    glenn_spends = wednesday_price + saturday_price

    # Return the result
    result = glenn_spends
    return result

print(solution())