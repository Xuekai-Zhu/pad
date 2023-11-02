def solution():
    """The Kwik-e-Tax Center charges $50 for a federal return, $30 for a state return, and $80 for quarterly business taxes. If they sell 60 federal returns, 20 state returns, and 10 quarterly returns in one day, what was their total revenue for the day?"""
    # Define the prices for each service
    FEDERAL_PRICE = 50
    STATE_PRICE = 30
    QUARTERLY_PRICE = 80

    # Calculate the revenue from federal returns
    federal_revenue = FEDERAL_PRICE * 60

    # Calculate the revenue from state returns
    state_revenue = STATE_PRICE * 20

    # Calculate the revenue from quarterly business taxes
    quarterly_revenue = QUARTERLY_PRICE * 10

    # Calculate the total revenue for the day
    total_revenue = federal_revenue + state_revenue + quarterly_revenue

    # return the result
    result = total_revenue
    return result

print(solution())