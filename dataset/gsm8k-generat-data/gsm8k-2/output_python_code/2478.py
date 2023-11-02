def solution():
    """The grocery store sells chips for $2 per packet and corn chips for $1.5 per packet. John would like to buy 15 packets of chips, and with the rest of the money he has left, buy as many packets of corn chips as he can. How many packets of corn chips could John buy if he has $45 for his entire purchase?"""
    chips_price = 2
    corn_chips_price = 1.5
    total_packets = 15
    total_money = 45
    chips_cost = total_packets * chips_price
    remaining_money = total_money - chips_cost
    corn_chips_packets = int(remaining_money / corn_chips_price)
    result = corn_chips_packets
    return result

print(solution())