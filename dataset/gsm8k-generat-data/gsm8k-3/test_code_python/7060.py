def solution():
    """Josh has $300 in his wallet, and $2000 invested in a business. If the business's stock price rises 30% and then he sells all of his stocks, how much money will he have in his wallet?"""
    # Define Josh's initial wallet and investment amounts
    wallet = 300
    investment = 2000

    # Calculate the new value of Josh's investment after a 30% increase in stock price
    new_investment_value = investment * 1.3

    # Sell all of Josh's stocks and add the proceeds to his wallet
    wallet += new_investment_value

    # Display the final amount in Josh's wallet
    result = wallet
    return result

print(solution())