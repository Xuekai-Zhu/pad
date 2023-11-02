def solution():
    
    uber_to_airport_time = 10
    airport_time = 5 * uber_to_airport_time
    bag_check_time = 15
    security_time = 3 * bag_check_time
    boarding_time = 20
    takeoff_time = 2 * boarding_time
    total_time = (uber_to_airport_time + airport_time + bag_check_time + security_time + boarding_time + takeoff_time) / 60
    result = total_time
    return result

print(solution())