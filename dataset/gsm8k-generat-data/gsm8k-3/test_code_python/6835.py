def solution():
    """The ski lift carries skiers all the way from the bottom of the mountain to the very top of the mountain, and then drops them off so they can ski back down the mountain. If it takes a skier 15 minutes to ride the lift from the bottom to the top of the mountain, and then it takes 5 minutes to ski back down the mountain, what is the most number of times a person can ski down the mountain in 2 hours?"""
    # Define the time it takes to ride the lift and ski down the mountain
    RIDE_TIME = 15
    SKI_TIME = 5

    # Calculate the total time available for skiing
    total_time = 2 * 60  # 2 hours in minutes

    # Calculate the time it takes for each round trip
    round_trip_time = RIDE_TIME + SKI_TIME

    # Calculate the maximum number of round trips possible in the total time available
    max_round_trips = total_time // round_trip_time

    # Display the maximum number of round trips
    result = max_round_trips
    return result

print(solution())