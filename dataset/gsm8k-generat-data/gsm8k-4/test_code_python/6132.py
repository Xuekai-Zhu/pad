def solution():
    """A married couple opened a savings account. The wife committed to saving $100 every week while the husband committed to saving $225 every month. After 4 months of savings, they decided to invest half of their money in buying stocks. Each share of stocks costs $50. How many shares of stocks can they buy?"""
    # Define the savings of the wife and the husband
    wife_savings = 100 * 4 * 0.5 # 4 weeks and 0.5 for half of the savings
    husband_savings = 225 * 4 * 0.5 # 4 months, 0.5 for half of the savings

    # Calculate the total savings
    total_savings = wife_savings + husband_savings

    # Calculate the number of shares they can buy
    shares = total_savings // 50

    # return the result
    result = shares
    return result

print(solution())