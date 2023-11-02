def solution():
    # Calculate the time it takes for Mary's Uber to get to her house
    uber_time = 10 / 60  # Convert 10 minutes to hours

    # Calculate the time it takes for Mary to get to the airport
    airport_time = 5 * uber_time

    # Calculate the time it takes for Mary to check her bag
    bag_time = 15 / 60  # Convert 15 minutes to hours

    # Calculate the time it takes for Mary to get through security
    security_time = 3 * bag_time

    # Calculate the time it takes for Mary to wait for her flight to start boarding
    boarding_time = 20 / 60  # Convert 20 minutes to hours

    # Calculate the time it takes for Mary to wait for the plane to take off
    takeoff_time = 2 * boarding_time

    # Calculate the total time for the entire process
    total_time = uber_time + airport_time + bag_time + security_time + boarding_time + takeoff_time
    result = total_time
    return result

print(solution())