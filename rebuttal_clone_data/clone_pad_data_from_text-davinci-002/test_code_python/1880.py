def solution():
     Milo_mph = Cory_mph / 2
     Milo_rolling_mph = Milo_mph * 2
     Milo_running_time = 2
     Milo_rolling_time = Milo_running_time / 2
     Cory_driving_time = Milo_running_time
     Cory_mph = 12
     Milo_distance = Milo_mph * Milo_running_time
     Milo_rolling_distance = Milo_rolling_mph * Milo_rolling_time
     Cory_distance = Cory_mph * Cory_driving_time
     result = Milo_distance + Milo_rolling_distance + Cory_distance
     return result

print(solution())