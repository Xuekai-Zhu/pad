def solution():
    """Mr. Grey's house was worth $100,000. He sold the house to Mr. Brown at a profit of 10%. After one year, Mr. Brown sold the house to his other friend with a 10% loss. How much was Mr. Brown's selling price?"""
    # Define the initial price of the house
    initial_price = 100000

    # Calculate Mr. Brown's buying price after the 10% profit
    brown_buying_price = initial_price * 1.1

    # Calculate Mr. Brown's selling price after the 10% loss
    brown_selling_price = brown_buying_price * 0.9

    result = brown_selling_price
    return result

print(solution())