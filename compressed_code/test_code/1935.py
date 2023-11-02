def solution():
    
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