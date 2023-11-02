def solution():
    """During one day, there are 4 boat trips through the lake. The boat can take up to 12 people during one trip. How many people can the boat transport in 2 days?"""
    # Define the number of boat trips and the maximum capacity of the boat
    boat_trips = 4
    boat_capacity = 12

    # Calculate the number of people the boat can transport in one day
    daily_capacity = boat_trips * boat_capacity

    # Calculate the number of people the boat can transport in two days
    total_capacity = daily_capacity * 2

    result = total_capacity
    return result

print(solution())