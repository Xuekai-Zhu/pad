def solution():
    
    amox_100_price = 5
    amox_500_price = 2
    weekly_amox_100_profit = 80
    weekly_amox_500_profit = 60
    weekly_amox_100_qty = weekly_amox_100_profit / amox_100_price
    weekly_amox_500_qty = weekly_amox_500_profit / amox_500_price
    total_qty = (weekly_amox_100_qty + weekly_amox_500_qty) * 2
    result = total_qty
    return result

print(solution())