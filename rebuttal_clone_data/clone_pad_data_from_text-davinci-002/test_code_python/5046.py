def solution():
     total_volume = 15000
     flow_rate_1 = 2
     flow_rate_2 = 3
     total_flow_rate = flow_rate_1 + flow_rate_2
     hours_to_fill = total_volume / total_flow_rate
     result = hours_to_fill
     return result

print(solution())