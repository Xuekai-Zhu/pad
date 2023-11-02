def solution():
     time_to_park = 5
     time_to_walk = 3
     time_to_get_through_metal_detector = 10
     
     time_in_minutes = time_to_park + time_to_walk + time_to_get_through_metal_detector
     
     result = time_in_minutes * 5
     return result

print(solution())