def solution():
     old_shoe_speed = 6
     new_shoe_speed = old_shoe_speed * 2
     blister_rate = 2
     hike_time = 4
     total_blisters = hike_time / blister_rate
     slow_down_speed = total_blisters * 2
     final_speed = new_shoe_speed - slow_down_speed
     result = final_speed
     
     return result

print(solution())