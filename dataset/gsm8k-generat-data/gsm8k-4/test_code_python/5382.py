def solution():
    """Emily is on a flight from New York to Hawaii that is 10 hours long. To kill time, she watches 3 TV episodes that are each 25 minutes long. Then she sleeps for 4 and a half hours. Then she watches 2 movies that are each an hour and 45 minutes long. After doing all these things, assuming there is no break time between activities, how many more minutes are left in the flight before Emily reaches Hawaii."""
    # Define the length of the flight in minutes
    flight_length = 10 * 60

    # Calculate the total time spent watching TV episodes
    tv_time = 3 * 25

    # Calculate the total time spent sleeping
    sleep_time = 4.5 * 60

    # Calculate the total time spent watching movies
    movie_time = 2 * 105

    # Calculate the total time spent on all activities
    total_time = tv_time + sleep_time + movie_time

    # Calculate the remaining time in the flight
    remaining_time = flight_length - total_time

    # return the result in minutes
    result = remaining_time
    return result

print(solution())