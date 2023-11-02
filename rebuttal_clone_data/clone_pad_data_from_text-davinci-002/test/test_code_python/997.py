def solution():
     packets_per_day = 2
     days = 90
     packets_per_box = 30
     cost_per_box = 4
     total_packets = packets_per_day * days
     total_boxes = total_packets / packets_per_box
     cost = total_boxes * cost_per_box
     result = cost
     return result

print(solution())