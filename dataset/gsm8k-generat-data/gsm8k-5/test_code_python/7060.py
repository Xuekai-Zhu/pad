def solution():
    wallet_money = 300  # Josh has $300 in his wallet
    invested_money = 2000  # Josh has $2000 invested in a business
    stock_price_increase = 0.3  # The stock price rises by 30%
    
    # Calculate the new value of Josh's investment after the stock price increase
    new_investment_value = invested_money + (invested_money * stock_price_increase)
    
    # Add the value of Josh's investment to the money in his wallet
    total_money = wallet_money + new_investment_value
    
    result = total_money
    return result

print(solution())