def solution():
    num_federal_returns = 60
    fee_federal_return = 50
    num_state_returns = 20
    fee_state_return = 30
    num_quarterly_returns = 10
    fee_quarterly_return = 80
    total_revenue = (num_federal_returns * fee_federal_return) + (num_state_returns * fee_state_return) + (num_quarterly_returns * fee_quarterly_return)
    
    result = total_revenue
    return result

print(solution())