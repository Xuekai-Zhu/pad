def solution():
    # Calculate the total number of hours the spacecraft traveled
    earth_day_hours = 24
    total_hours = 2 * earth_day_hours - 8  # traveled in 8 hours less than twice the number of hours in a typical earth day

    # Calculate the average speed of the spacecraft
    distance = 4000  # parsecs
    speed = distance / total_hours
    result = speed
    return result

print(solution())