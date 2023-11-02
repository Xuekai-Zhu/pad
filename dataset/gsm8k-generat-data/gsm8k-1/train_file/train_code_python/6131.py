def solution():
    """
    A married couple opened a savings account. The wife committed to saving $100 every week while the husband committed to saving $225 every month. 
    After 4 months of savings, they decided to invest half of their money in buying stocks. Each share of stocks costs $50. How many shares of stocks can they buy?
    """
    weekly_savings = 100
    monthly_savings = 225
    savings_in_4_months = (weekly_savings * 4 * 4) + (monthly_savings * 4)
    half_of_savings = savings_in_4_months / 2
    shares_of_stock = half_of_savings / 50
    result = shares_of_stock
    
    return result

print(solution())