def solution():
    """Some friends wanted to make a road trip from New York to Los Angeles. They drove at a constant speed of 62 miles/hour, taking breaks of 30 minutes every 5 hours. Once in the city, they looked for the hotel for 30 minutes. If the trip took around 2,790 miles, how many hours will they have to spend to complete the trip to the hotel?"""
    trip_distance = 2790
    driving_speed = 62
    driving_time = trip_distance / driving_speed
    num_breaks = driving_time // 5
    break_time = num_breaks * 0.5
    hotel_search_time = 0.5
    total_time = driving_time + break_time + hotel_search_time
    result = total_time
    return result

print(solution())