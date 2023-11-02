def solution():
    """Emily is on a flight from New York to Hawaii that is 10 hours long. To kill time, she watches 3 TV episodes that are each 25 minutes long. Then she sleeps for 4 and a half hours. Then she watches 2 movies that are each an hour and 45 minutes long. After doing all these things, assuming there is no break time between activities, how many more minutes are left in the flight before Emily reaches Hawaii."""
    # Define the length of each TV episode and movie in minutes
    TV_EPISODE_LENGTH = 25
    MOVIE_LENGTH = 105

    # Define the length of time Emily slept in minutes
    SLEEP_LENGTH = 270

    # Calculate the total time Emily spent watching TV
    tv_time = 3 * TV_EPISODE_LENGTH

    # Calculate the total time Emily spent watching movies
    movie_time = 2 * MOVIE_LENGTH

    # Calculate the total time Emily spent on activities
    total_time = tv_time + SLEEP_LENGTH + movie_time

    # Calculate the remaining time in minutes
    remaining_time = (10 * 60) - total_time

    # Display the remaining time in minutes
    result = remaining_time
    return result

print(solution())