def solution():
    """The Kwik-e-Tax Center charges $50 for a federal return, $30 for a state return, and $80 for quarterly business taxes. If they sell 60 federal returns, 20 state returns, and 10 quarterly returns in one day, what was their total revenue for the day?"""
    federal_price = 50
    state_price = 30
    quarterly_price = 80
    
    federal_returns = 60
    state_returns = 20
    quarterly_returns = 10
    
    federal_revenue = federal_price * federal_returns
    state_revenue = state_price * state_returns
    quarterly_revenue = quarterly_price * quarterly_returns
    
    total_revenue = federal_revenue + state_revenue + quarterly_revenue
    
    result = total_revenue
    return result

print(solution())