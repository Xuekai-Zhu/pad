def solution():
    Jenna_miles_per_hour = 50
    friend_miles_per_hour = 20
    total_miles = 200 + 100
    travel_time = total_miles / (Jenna_miles_per_hour + friend_miles_per_hour)
    stops = 2
    stop_time = stops * 0.5
    total_time = travel_time + stop_time
    result = total_time
    return result

print(solution())