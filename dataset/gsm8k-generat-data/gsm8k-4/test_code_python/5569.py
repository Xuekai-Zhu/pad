def solution():
    """Some friends wanted to make a road trip from New York to Los Angeles. They drove at a constant speed of 62 miles/hour, taking breaks of 30 minutes every 5 hours. Once in the city, they looked for the hotel for 30 minutes. If the trip took around 2,790 miles, how many hours will they have to spend to complete the trip to the hotel?"""
    # Define the constants
    SPEED = 62
    BREAK_TIME = 0.5
    BREAK_INTERVAL = 5
    HOTEL_SEARCH_TIME = 0.5

    # Calculate the total travel time without breaks
    travel_time = 2790 / SPEED

    # Calculate the number of breaks they will take
    num_breaks = travel_time // BREAK_INTERVAL

    # Calculate the total time of all breaks
    total_break_time = num_breaks * BREAK_TIME

    # Add the time spent looking for the hotel
    total_time = travel_time + total_break_time + HOTEL_SEARCH_TIME

    result = total_time
    return result

print(solution())