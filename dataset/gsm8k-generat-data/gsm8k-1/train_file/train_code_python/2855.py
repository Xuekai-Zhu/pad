def solution():
    """Mary is going on a business trip. It takes 10 minutes for her Uber to get to her house and 5 times longer to get to the airport. It takes 15 minutes to check her bag and three times as long to get through security. Then she has to wait for 20 minutes for her flight to start boarding and twice as long before the plane is ready to take off. How many hours will this process take total?"""
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