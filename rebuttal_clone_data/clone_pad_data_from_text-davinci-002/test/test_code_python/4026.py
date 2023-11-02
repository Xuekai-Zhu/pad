def solution():
     heavy_traffic_time = 5
     no_traffic_time = 4
     total_time = heavy_traffic_time + no_traffic_time
     heavy_traffic_speed = 200 / heavy_traffic_time
     no_traffic_speed = 200 / no_traffic_time
     average_speed = (heavy_traffic_speed + no_traffic_speed) / 2
     difference_in_speed = no_traffic_speed - heavy_traffic_speed
     result = difference_in_speed
     return result

print(solution())