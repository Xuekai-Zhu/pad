def solution():
    wallet_money = 300
    initial_investment = 2000
    stock_rise = 0.3  # 30% increase in stock price

    # Calculate the new value of the investment after the stock price rise
    new_value = initial_investment * (1 + stock_rise)

    # Calculate the total amount of money Josh will have after selling all his stocks
    total_money = wallet_money + new_value
    result = total_money
    return result

print(solution())