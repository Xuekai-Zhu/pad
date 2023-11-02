def solution():
    # Calculate the total amount saved by the wife in 4 months
    wife_total_savings = 100 * 4

    # Calculate the total amount saved by the husband in 4 months
    husband_total_savings = 225 * 4

    # Calculate their total savings after 4 months
    total_savings = wife_total_savings + husband_total_savings

    # Calculate the amount to be invested in stocks
    stocks_investment = total_savings / 2

    # Calculate the number of shares they can buy
    shares = stocks_investment / 50
    result = shares
    return result

print(solution())