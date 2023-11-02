def solution():
    """Some friends wanted to make a road trip from New York to Los Angeles. They drove at a constant speed of 62 miles/hour, taking breaks of 30 minutes every 5 hours. Once in the city, they looked for the hotel for 30 minutes. If the trip took around 2,790 miles, how many hours will they have to spend to complete the trip to the hotel?"""
    speed = 62
    total_distance = 2790
    breaks_every = 5
    break_time = 0.5 # 30 min is half hour
    hotel_finding_time = 0.5 # 30 min is half hour
    time_without_breaks = total_distance / speed
    number_of_breaks = time_without_breaks // breaks_every
    total_time = time_without_breaks + (number_of_breaks * break_time) + hotel_finding_time
    result = total_time
    return result

print(solution())