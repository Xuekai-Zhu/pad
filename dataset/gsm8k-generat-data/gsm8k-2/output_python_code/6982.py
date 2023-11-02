def solution():
    """A Ferris wheel can accommodate 70 people in 20 minutes. If the Ferris wheel is open from 1:00 pm until 7:00 pm, how many people will get to ride?"""
    ride_capacity = 70
    ride_duration = 20
    open_hours = 6  # from 1:00 pm to 7:00 pm is 6 hours
    total_minutes = open_hours * 60
    total_riders = (total_minutes // ride_duration) * ride_capacity
    result = total_riders
    return result

print(solution())