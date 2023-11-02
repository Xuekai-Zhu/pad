def solution():
     start_time = 1
     end_time = start_time + 5
     hour_1 = 2
     hours_2_5 = 1
     hours_6_9 = 3
     tank_height = 18
     total_rainfall = hour_1 + (hours_2_5 * 4) + (hours_6_9 * 4)
 
     if total_rainfall >= tank_height:
         time_filled = end_time
     else:
         time_filled = "Tank will not be full"
 
     result = time_filled
     return result

print(solution())