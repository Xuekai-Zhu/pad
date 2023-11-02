def solution():
    """A fruit stand is selling apples for $2 each. Emmy has $200 while Gerry has $100. If they want to buy apples, how many apples can Emmy and Gerry buy altogether?"""
    # Define the price per apple and the amount of money Emmy and Gerry have
    APPLE_PRICE = 2
    EMMY_MONEY = 200
    GERRY_MONEY = 100

    # Calculate the maximum number of apples that Emmy and Gerry can buy
    max_apples = (EMMY_MONEY + GERRY_MONEY) // APPLE_PRICE

    # Return the result
    result = max_apples
    return result

print(solution())