def solution():
    """Mr. Grey's house was worth $100,000. He sold the house to Mr. Brown at a profit of 10%. After one year, Mr. Brown sold the house to his other friend with a 10% loss. How much was Mr. Brown's selling price?"""
    initial_price = 100000
    profit_percent = 10
    selling_price_1 = initial_price * (1 + (profit_percent / 100))
    loss_percent = 10
    selling_price_2 = selling_price_1 * (1 - (loss_percent / 100))
    result = selling_price_2
    return result

print(solution())