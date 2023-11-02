def solution():
    """The Kwik-e-Tax Center charges $50 for a federal return, $30 for a state return, and $80 for quarterly business taxes. If they sell 60 federal returns, 20 state returns, and 10 quarterly returns in one day, what was their total revenue for the day?"""
    # Define the prices for each type of return
    FEDERAL_PRICE = 50
    STATE_PRICE = 30
    QUARTERLY_PRICE = 80

    # Define the number of each type of return sold in one day
    federal_returns = 60
    state_returns = 20
    quarterly_returns = 10

    # Calculate the total revenue for the day
    total_revenue = (federal_returns * FEDERAL_PRICE) + (state_returns * STATE_PRICE) + (quarterly_returns * QUARTERLY_PRICE)

    # Display the total revenue for the day
    result = total_revenue
    return result

print(solution())