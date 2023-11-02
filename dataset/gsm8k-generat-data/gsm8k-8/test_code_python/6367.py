def solution():
    # Calculate the price Bert paid for the barrel in the warehouse
    warehouse_price = 90 - 10

    # Calculate the price Bert sold the barrel for in his shop
    shop_price = warehouse_price + 10

    # Calculate the amount of tax Bert has to pay on the sale
    tax = shop_price * 0.1

    # Calculate the profit Bert made on the sale
    profit = shop_price - warehouse_price - tax
    result = profit
    return result

print(solution())