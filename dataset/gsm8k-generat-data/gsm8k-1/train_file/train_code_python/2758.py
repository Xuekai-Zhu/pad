def solution():
    """To get to work, Ryan bikes one day a week takes the bus three times a week and gets a ride from a friend once a week. It takes him thirty minutes to bike to work. The bus takes ten minutes longer since it stops at every bus stop for other passengers. His friend driving him is the fastest and cuts two-thirds off his biking time. How many minutes does he spend every week commuting to work?"""
    bike_day = 1
    bus_day = 3
    ride_day = 1
    bike_time = 30
    bus_time = bike_time + 10
    ride_time = bike_time * (1/3)
    total_time = (bike_day * bike_time) + (bus_day * bus_time) + (ride_day * ride_time)
    result = total_time
    return result

print(solution())