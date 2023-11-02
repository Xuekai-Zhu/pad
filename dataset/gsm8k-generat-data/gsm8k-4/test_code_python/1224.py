def solution():
    """Jim starts with $80 in his investment portfolio. After 1 year it grows by 15%. He then adds another $28 to his portfolio. After 1 more year the combined portfolio grows by 10%. What is his final portfolio worth after 2 years from when he started?"""
    # Define the initial portfolio value and the growth rate
    initial_portfolio = 80
    growth_rate = 0.15

    # Calculate the portfolio value after 1 year
    portfolio_after_1_year = initial_portfolio * (1 + growth_rate)

    # Add the $28 to the portfolio after 1 year
    portfolio_after_1_year += 28

    # Calculate the portfolio value after 2 years
    growth_rate_2 = 0.1
    portfolio_after_2_years = portfolio_after_1_year * (1 + growth_rate_2)

    # return the result
    result = portfolio_after_2_years
    return result

print(solution())