def solution():
    """Mr. Grey's house was worth $100,000. He sold the house to Mr. Brown at a profit of 10%. After one year, Mr. Brown sold the house to his other friend with a 10% loss. How much was Mr. Brown's selling price?"""
    grey_price = 100000
    brown_profit = 0.1
    brown_price = grey_price + (brown_profit * grey_price)
    friend_loss = 0.1
    friend_price = brown_price - (friend_loss * brown_price)
    result = friend_price
    return result

print(solution())