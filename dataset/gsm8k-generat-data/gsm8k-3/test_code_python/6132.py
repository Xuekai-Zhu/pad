def solution():
    """A married couple opened a savings account. The wife committed to saving $100 every week while the husband committed to saving $225 every month. After 4 months of savings, they decided to invest half of their money in buying stocks. Each share of stocks costs $50. How many shares of stocks can they buy?"""
    # Calculate the total savings of the wife after 4 months
    wife_savings = 4 * 100 * 4  # 4 weeks in a month

    # Calculate the total savings of the husband after 4 months
    husband_savings = 225 * 4

    # Calculate the total savings of the couple
    total_savings = wife_savings + husband_savings

    # Calculate the amount they will invest in buying stocks
    stock_investment = total_savings / 2

    # Calculate the number of shares of stocks they can buy
    num_shares = stock_investment / 50

    # Display the number of shares they can buy
    result = num_shares
    return result

print(solution())