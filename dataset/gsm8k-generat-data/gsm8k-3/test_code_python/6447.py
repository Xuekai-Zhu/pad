def solution():
    """A fruit stand is selling apples for $2 each. Emmy has $200 while Gerry has $100. If they want to buy apples, how many apples can Emmy and Gerry buy altogether?"""
    # Define the price of each apple and the amount of money each person has
    APPLE_PRICE = 2
    EMMY_MONEY = 200
    GERRY_MONEY = 100

    # Calculate the maximum number of apples each person can buy
    emmy_apples = EMMY_MONEY // APPLE_PRICE
    gerry_apples = GERRY_MONEY // APPLE_PRICE

    # Calculate the total number of apples they can buy together
    total_apples = emmy_apples + gerry_apples

    # Display the total number of apples they can buy
    result = total_apples
    return result

print(solution())