def solution():
    chips_price = 2
    corn_chips_price = 1.5
    num_chips_packets = 15
    total_purchase_money = 45

    # Calculate the total cost of all chips packets
    total_chips_cost = num_chips_packets * chips_price

    # Calculate the amount of money left after buying all chips packets
    money_left = total_purchase_money - total_chips_cost

    # Calculate the maximum number of corn chips packets that can be bought with the remaining money
    num_corn_chips_packets = money_left // corn_chips_price
    result = num_corn_chips_packets
    return result

print(solution())