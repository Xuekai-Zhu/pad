def solution():
    """A woman is trying to decide whether it will be quicker to take an airplane or drive herself to a job interview. If she drives herself, the trip will take her 3 hours and 15 minutes.  If she takes an airplane, she will first need to drive 10 minutes to the airport, and then wait 20 minutes to board the plane.  After that, she will be on the airplane for one-third of the time it would have taken her to drive herself before landing in the destination city. Finally, it will take her an additional 10 minutes to get off the airplane and arrive at her interview site after the plane lands.  Given this information, how many minutes faster is it for her to take the airplane?"""
    # Define the time it takes to drive to the interview
    drive_time = 3 * 60 + 15 # Convert 3 hours and 15 minutes to minutes

    # Calculate the time it takes to fly to the interview
    fly_time = 10 + 20 # Time to drive to airport and wait to board the plane
    fly_time += (drive_time / 3) # Time on the airplane
    fly_time += 10 # Time to get off the airplane and arrive at the interview site

    # Calculate the difference in time
    time_difference = drive_time - fly_time

    # Display the time difference in minutes
    result = time_difference
    return result

print(solution())