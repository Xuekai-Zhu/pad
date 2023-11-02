def solution():
    """Mary is going on a business trip. It takes 10 minutes for her Uber to get to her house and 5 times longer to get to the airport. It takes 15 minutes to check her bag and three times as long to get through security.
    Then she has to wait for 20 minutes for her flight to start boarding and twice as long before the plane is ready to take off. How many hours will this process take total?"""
    # Define the time in minutes for each step of the process
    uber_time = 10
    airport_time = uber_time * 5
    check_bag_time = 15
    security_time = check_bag_time * 3
    boarding_time = 20
    takeoff_time = boarding_time * 2

    # Calculate the total time in minutes
    total_time = uber_time + airport_time + check_bag_time + security_time + boarding_time + takeoff_time

    # Convert the total time to hours
    hours = total_time / 60

    # Return the result
    result = hours
    return result

print(solution())