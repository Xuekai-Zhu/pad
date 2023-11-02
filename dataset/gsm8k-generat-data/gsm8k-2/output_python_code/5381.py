def solution():
    """Emily is on a flight from New York to Hawaii that is 10 hours long. To kill time, she watches 3 TV episodes that are each 25 minutes long. Then she sleeps for 4 and a half hours. Then she watches 2 movies that are each an hour and 45 minutes long. After doing all these things, assuming there is no break time between activities, how many more minutes are left in the flight before Emily reaches Hawaii."""
    flight_time = 10*60
    tv_episode_time = 3 * 25
    sleep_time = 4.5 * 60
    movie_time = 2 * 105
    total_time_spent = tv_episode_time + sleep_time + movie_time
    remaining_time = flight_time - total_time_spent
    result = remaining_time
    return result

print(solution())