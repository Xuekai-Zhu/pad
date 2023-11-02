def solution():
    """Mr. Grey's house was worth $100,000. He sold the house to Mr. Brown at a profit of 10%. After one year, Mr. Brown sold the house to his other friend with a 10% loss. How much was Mr. Brown's selling price?"""
    # Define the original price of the house and the profit percentage
    ORIGINAL_PRICE = 100000
    PROFIT_PERCENTAGE = 0.1

    # Calculate the selling price of the house to Mr. Brown
    brown_buying_price = ORIGINAL_PRICE * (1 + PROFIT_PERCENTAGE)

    # Calculate the selling price of the house from Mr. Brown to his friend
    friend_selling_price = brown_buying_price * 0.9

    # Display Mr. Brown's selling price
    result = friend_selling_price
    return result

print(solution())