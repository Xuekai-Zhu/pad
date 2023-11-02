def solution():
    # Calculate the total amount saved by the wife in 4 months
    savings_wife = 100 * 4 * 4  # $100 every week for 4 months

    # Calculate the total amount saved by the husband in 4 months
    savings_husband = 225 * 4

    # Calculate the total savings after 4 months
    total_savings = savings_wife + savings_husband

    # Calculate the amount to be invested in stocks
    stocks_investment = total_savings / 2

    # Calculate the number of shares of stocks that can be bought
    shares_bought = stocks_investment / 50
    result = shares_bought
    return result

print(solution())