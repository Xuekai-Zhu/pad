def solution():
    initial_portfolio = 80
    growth_rate_1 = 0.15
    additional_contribution = 28
    growth_rate_2 = 0.1

    # Calculate the portfolio value after the first year of growth
    portfolio_1 = initial_portfolio * (1 + growth_rate_1)

    # Calculate the portfolio value after the additional contribution and second year of growth
    portfolio_2 = (portfolio_1 + additional_contribution) * (1 + growth_rate_2)

    # Calculate the final portfolio value after 2 years
    final_portfolio = round(portfolio_2, 2)
    result = final_portfolio
    return result

print(solution())