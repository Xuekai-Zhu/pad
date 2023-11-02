def solution():
    
    chips_price = 2
    corn_chips_price = 1.5
    total_packets = 15
    total_budget = 45
    chips_cost = total_packets * chips_price
    corn_chips_budget = total_budget - chips_cost
    corn_chips_packets = corn_chips_budget // corn_chips_price
    result = corn_chips_packets
    return result

print(solution())