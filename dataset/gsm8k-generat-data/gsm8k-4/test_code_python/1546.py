def solution():
    """A woman is trying to decide whether it will be quicker to take an airplane or drive herself to a job interview. If she drives herself, the trip will take her 3 hours and 15 minutes. If she takes an airplane, she will first need to drive 10 minutes to the airport, and then wait 20 minutes to board the plane. After that, she will be on the airplane for one-third of the time it would have taken her to drive herself before landing in the destination city. Finally, it will take her an additional 10 minutes to get off the airplane and arrive at her interview site after the plane lands. Given this information, how many minutes faster is it for her to take the airplane?"""
    # Define the time it takes to drive to the interview site
    drive_time = 3 * 60 + 15

    # Define the time it takes to drive to the airport and board the plane
    airport_time = 10 + 20

    # Define the time it takes to fly to the destination city
    flight_time = drive_time / 3

    # Define the time it takes to get off the airplane and arrive at the interview site
    landing_time = 10

    # Calculate the total time it takes to take the airplane
    airplane_time = airport_time + flight_time + landing_time

    # Calculate the time saved by taking the airplane
    time_saved = drive_time - airplane_time

    # Return the result in minutes
    result = time_saved
    return result

print(solution())