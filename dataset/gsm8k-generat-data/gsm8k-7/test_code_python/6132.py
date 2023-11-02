def solution():
    wife_weekly_savings = 100
    husband_monthly_savings = 225
    num_months_saving = 4
    stock_price = 50

    # Calculate the total amount saved by the wife
    total_wife_savings = wife_weekly_savings * 4 * num_months_saving

    # Calculate the total amount saved by the husband
    total_husband_savings = husband_monthly_savings * num_months_saving

    # Calculate the total amount saved by the couple
    total_savings = total_wife_savings + total_husband_savings

    # Calculate the amount to be invested in stocks
    stocks_investment = total_savings / 2

    # Calculate the number of shares of stocks they can buy
    num_shares = stocks_investment // stock_price
    result = num_shares
    return result

print(solution())