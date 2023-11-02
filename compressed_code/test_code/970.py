def solution():
    
    federal_price = 50
    state_price = 30
    quarterly_price = 80
    federal_returns = 60
    state_returns = 20
    quarterly_returns = 10
    total_revenue = (federal_price * federal_returns) + (state_price * state_returns) + (quarterly_price * quarterly_returns)
    result = total_revenue
    return result

print(solution())