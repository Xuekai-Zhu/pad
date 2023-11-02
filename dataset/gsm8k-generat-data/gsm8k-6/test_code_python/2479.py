def solution():
    # Calculate how much John will spend on chips
    chips_price = 2  # price of chips per packet
    chips_quantity = 15  # number of packets of chips John wants to buy
    chips_total_price = chips_price * chips_quantity

    # Calculate how much John will have left to spend on corn chips
    remaining_money = 45 - chips_total_price

    # Calculate how many packets of corn chips John can buy
    corn_chips_price = 1.5  # price of corn chips per packet
    corn_chips_quantity = remaining_money / corn_chips_price
    result = corn_chips_quantity
    return result

print(solution())