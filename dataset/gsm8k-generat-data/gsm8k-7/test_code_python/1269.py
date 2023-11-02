def solution():
    federal_price = 50
    state_price = 30
    quarterly_price = 80

    num_federal_returns = 60
    num_state_returns = 20
    num_quarterly_returns = 10

    # Calculate the total revenue from federal returns
    total_federal_revenue = num_federal_returns * federal_price

    # Calculate the total revenue from state returns
    total_state_revenue = num_state_returns * state_price

    # Calculate the total revenue from quarterly returns
    total_quarterly_revenue = num_quarterly_returns * quarterly_price

    # Calculate the total revenue for the day
    total_revenue = total_federal_revenue + total_state_revenue + total_quarterly_revenue
    result = total_revenue
    return result

print(solution())