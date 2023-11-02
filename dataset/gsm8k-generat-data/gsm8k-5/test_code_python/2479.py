def solution():
    chips_cost = 2  # Chips cost $2 per packet
    corn_chips_cost = 1.5  # Corn chips cost $1.5 per packet
    total_packets = 15  # John wants to buy 15 packets of chips
    total_cost = 45  # John has $45 to spend

    # Calculate the number of chips John can buy
    chips_count = total_packets
    chips_price = chips_count * chips_cost

    # Calculate the number of corn chips John can buy with the remaining money
    remaining_money = total_cost - chips_price
    corn_chips_count = int(remaining_money / corn_chips_cost)
    result = corn_chips_count
    return result

print(solution())