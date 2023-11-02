def solution():
     ice_cream_cone_melt_time = 10
     blocks_to_beach = 16
     one_block = 1 / 8
     miles_to_beach = blocks_to_beach * one_block
     minutes_to_hour = 60
     seconds_to_minute = 60
     hour_to_second = minutes_to_hour * seconds_to_minute
     miles_per_second = miles_to_beach / hour_to_second
     hours_to_seconds = 1 / miles_per_second
     result = hours_to_seconds
     return result

print(solution())