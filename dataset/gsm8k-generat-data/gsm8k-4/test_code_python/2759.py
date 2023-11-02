def solution():
    """To get to work, Ryan bikes one day a week takes the bus three times a week and gets a ride from a friend once a week. It takes him thirty minutes to bike to work. The bus takes ten minutes longer since it stops at every bus stop for other passengers. His friend driving him is the fastest and cuts two-thirds off his biking time. How many minutes does he spend every week commuting to work?"""
    # Define the time it takes to bike, take the bus, and get a ride from a friend
    bike_time = 30
    bus_time = bike_time + 10
    friend_time = bike_time * (1 - 2/3)

    # Calculate the total time spent commuting each week
    total_time = bike_time + bus_time * 3 + friend_time

    # Return the result in minutes
    result = total_time
    return result

print(solution())