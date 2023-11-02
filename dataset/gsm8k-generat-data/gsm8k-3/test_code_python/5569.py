def solution():
    """Some friends wanted to make a road trip from New York to Los Angeles. They drove at a constant speed of 62 miles/hour, taking breaks of 30 minutes every 5 hours. Once in the city, they looked for the hotel for 30 minutes. If the trip took around 2,790 miles, how many hours will they have to spend to complete the trip to the hotel?"""
    # Define the speed of the car
    speed = 62

    # Define the duration of breaks
    break_duration = 0.5 # hours

    # Define the duration of hotel search
    hotel_search_duration = 0.5 # hours

    # Define the distance of the trip
    distance = 2790 # miles

    # Calculate the total duration of breaks
    total_break_duration = (distance // 5) * break_duration

    # Calculate the total duration of the trip
    total_trip_duration = (distance / speed) + total_break_duration + hotel_search_duration

    # Display the total duration of the trip
    result = total_trip_duration
    return result

print(solution())