def solution():
    
    uber_time = 10
    airport_time = 5 * uber_time
    bag_check_time = 15
    security_time = 3 * bag_check_time
    boarding_time = 20
    plane_ready_time = 2 * boarding_time
    total_time = (uber_time + airport_time + bag_check_time + security_time + boarding_time + plane_ready_time) / 60
    result = total_time
    return result

print(solution())