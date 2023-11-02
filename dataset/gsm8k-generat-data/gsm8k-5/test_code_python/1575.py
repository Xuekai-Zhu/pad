def solution(): 
    # Total weight of wool produced
    total_wool_weight = 200 * 10  # 200 sheep, each producing 10 pounds of wool
    
    # Total revenue from selling the wool
    total_revenue = total_wool_weight * 20  # $20 per pound of wool
    
    # Profit after paying the shearer
    profit = total_revenue - 2000
    
    result = profit
    return result

print(solution())