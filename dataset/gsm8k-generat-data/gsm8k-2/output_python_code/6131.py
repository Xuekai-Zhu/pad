def solution():
    """A married couple opened a savings account. The wife committed to saving $100 every week while the husband committed to saving $225 every month. After 4 months of savings, they decided to invest half of their money in buying stocks. Each share of stocks costs $50. How many shares of stocks can they buy?"""
    wife_savings = 100 * 4 * 4  # 4 months, $100 every week
    husband_savings = 225 * 4  # 4 months, $225 every month
    total_savings = wife_savings + husband_savings
    investment_amount = total_savings / 2
    shares = investment_amount / 50
    result = shares
    return result

print(solution())