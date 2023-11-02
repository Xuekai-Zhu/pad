def solution():
     old_bridge_capacity = 2000
     new_bridge_capacity = 2 * old_bridge_capacity
     percent_increase = 60
     new_bridge_traffic = old_bridge_capacity + (old_bridge_capacity * (percent_increase / 100))
     total_traffic = new_bridge_traffic + old_bridge_capacity
     result = total_traffic
     
     return result

print(solution())