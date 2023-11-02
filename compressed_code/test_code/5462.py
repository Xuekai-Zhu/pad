def solution():
    
    wallet_money = 300
    investment_money = 2000
    stock_price_increase = 0.3
    final_investment_money = investment_money * (1 + stock_price_increase)
    total_money = wallet_money + final_investment_money
    result = total_money
    return result

print(solution())