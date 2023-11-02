def solution():
     store_buy_price = 20
     store_profit_percent = 30
     store_sale_percent = 50
     store_sale_price = store_buy_price + store_buy_price * store_profit_percent * (store_sale_percent / 100)
     store_sale_price = store_sale_price * (store_sale_percent / 100)
     result = store_sale_price
     return result

print(solution())