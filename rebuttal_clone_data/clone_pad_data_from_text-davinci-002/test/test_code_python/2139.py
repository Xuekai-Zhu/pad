def solution():
     overage_mph = 10
     time_traveled = 1
     distance_traveled = 60
     mph  = distance_traveled / time_traveled
     speed_limit = mph - overage_mph
     result = speed_limit
     return result

print(solution())