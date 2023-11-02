def solution():
    # Calculate the number of 100 mg capsules sold
    amox_100_profit = 80
    amox_100_price = 5
    amox_100_qty = amox_100_profit / amox_100_price

    # Calculate the number of 500 mg capsules sold
    amox_500_profit = 60
    amox_500_price = 2
    amox_500_qty = amox_500_profit / amox_500_price

    # Calculate the total number of capsules sold every 2 weeks
    total_qty = (amox_100_qty + amox_500_qty) * 2
    result = total_qty
    return result

print(solution())