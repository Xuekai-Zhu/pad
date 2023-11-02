def solution():
     initial_wallet_amount = 300
     initial_stock_amount = 2000
     stock_percent_increase = 30
     stock_amount_after_increase = initial_stock_amount * (1 + (stock_percent_increase / 100))
     wallet_amount_after_sale = initial_wallet_amount + stock_amount_after_increase
     result = wallet_amount_after_sale
     return result

print(solution())