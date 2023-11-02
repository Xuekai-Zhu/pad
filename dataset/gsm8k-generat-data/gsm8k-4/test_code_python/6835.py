def solution():
    """The ski lift carries skiers all the way from the bottom of the mountain to the very top of the mountain, and then drops them off so they can ski back down the mountain. If it takes a skier 15 minutes to ride the lift from the bottom to the top of the mountain, and then it takes 5 minutes to ski back down the mountain, what is the most number of times a person can ski down the mountain in 2 hours?"""
    # Define the time it takes for one round trip
    round_trip_time = 15 + 5

    # Calculate the number of round trips that can be made in 2 hours
    max_round_trips = (2*60) // round_trip_time

    # Display the result
    result = max_round_trips
    return result

print(solution())