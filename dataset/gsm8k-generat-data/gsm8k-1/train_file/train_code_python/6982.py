def solution():
    """A Ferris wheel can accommodate 70 people in 20 minutes. If the Ferris wheel is open from 1:00 pm until 7:00 pm, how many people will get to ride?"""
    ride_per_20min = 70
    hour_opens = 1
    hour_closes = 7
    minutes_open = (hour_closes - hour_opens) * 60
    ride_per_minute = ride_per_20min / 20
    total_rides = ride_per_minute * minutes_open
    result = total_rides
    return result

print(solution())