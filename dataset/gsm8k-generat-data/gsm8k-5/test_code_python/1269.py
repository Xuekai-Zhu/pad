def solution():
    cost_federal_return = 50  # The cost of a federal return is $50
    cost_state_return = 30  # The cost of a state return is $30
    cost_quarterly_taxes = 80  # The cost of quarterly business taxes is $80
    quantity_federal_return = 60  # The Kwik-e-Tax Center sells 60 federal returns in one day
    quantity_state_return = 20  # The Kwik-e-Tax Center sells 20 state returns in one day
    quantity_quarterly_taxes = 10  # The Kwik-e-Tax Center sells 10 quarterly returns in one day

    # Calculate the revenue from federal returns
    revenue_federal_return = cost_federal_return * quantity_federal_return

    # Calculate the revenue from state returns
    revenue_state_return = cost_state_return * quantity_state_return

    # Calculate the revenue from quarterly returns
    revenue_quarterly_taxes = cost_quarterly_taxes * quantity_quarterly_taxes

    # Calculate the total revenue for the day
    total_revenue = revenue_federal_return + revenue_state_return + revenue_quarterly_taxes
    result = total_revenue
    return result

print(solution())