def solution():
    # Calculate the total revenue for the day
    revenue_federal = 50 * 60  # 60 federal returns at $50 each
    revenue_state = 30 * 20  # 20 state returns at $30 each
    revenue_quarterly = 80 * 10  # 10 quarterly business taxes at $80 each
    total_revenue = revenue_federal + revenue_state + revenue_quarterly
    result = total_revenue
    return result

print(solution())