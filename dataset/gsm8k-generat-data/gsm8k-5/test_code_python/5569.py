def solution():
    speed = 62  # They drove at a constant speed of 62 miles/hour
    distance = 2790  # The trip was around 2,790 miles
    time_without_breaks = distance / speed  # Calculate the time without considering the breaks and hotel search
    number_of_breaks = distance // (5 * 62)  # Calculate the number of breaks taken every 5 hours
    time_breaks = number_of_breaks * 0.5  # Calculate the time spent on breaks
    time_hotel = 0.5  # They looked for the hotel for 30 minutes
    total_time = time_without_breaks + time_breaks + time_hotel  # Calculate the total time including breaks and hotel search
    result = total_time
    return result

print(solution())