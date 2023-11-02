def solution():
    """Josh has $300 in his wallet, and $2000 invested in a business. If the business's stock price rises 30% and then he sells all of his stocks, how much money will he have in his wallet?"""
    # Define the initial amount of money in Josh's wallet and the amount invested in the business
    wallet_money = 300
    business_money = 2000

    # Calculate the increase in the stock price
    stock_increase = 0.3

    # Calculate the new value of the business after the stock price increase
    new_business_value = business_money + (business_money * stock_increase)

    # Add the new business value to the money in Josh's wallet
    total_money = wallet_money + new_business_value

    # Return the result
    result = total_money
    return result

print(solution())