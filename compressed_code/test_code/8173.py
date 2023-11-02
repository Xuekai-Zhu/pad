def solution():
    
    old_bridge_capacity = 2000 * 12  
    new_bridge_capacity = 2 * 5 * old_bridge_capacity  
    new_bridge_traffic = old_bridge_capacity * (1 + 0.6)  
    total_traffic = old_bridge_capacity + new_bridge_traffic
    result = total_traffic
    return result

print(solution())