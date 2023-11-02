def solution():
    """Josh has $300 in his wallet, and $2000 invested in a business. If the business's stock price rises 30% and then he sells all of his stocks, how much money will he have in his wallet?"""
    wallet_money = 300
    investment_money = 2000
    stock_price_increase = 30
    new_stock_price = investment_money * (1 + (stock_price_increase / 100))
    total_money = wallet_money + new_stock_price
    result = total_money
    return result

print(solution())