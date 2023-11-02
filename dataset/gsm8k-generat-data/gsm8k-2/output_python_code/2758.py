def solution():
    """To get to work, Ryan bikes one day a week takes the bus three times a week and gets a ride from a friend once a week. It takes him thirty minutes to bike to work. The bus takes ten minutes longer since it stops at every bus stop for other passengers. His friend driving him is the fastest and cuts two-thirds off his biking time. How many minutes does he spend every week commuting to work?"""
    bike_time = 30
    bus_time = bike_time + 10
    friend_time = bike_time - (2/3 * bike_time)
    total_time = bike_time + (3 * bus_time) + friend_time
    result = total_time
    return result

print(solution())