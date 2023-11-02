def solution():
    miles_to_friend = 30
    miles_on_detour = miles_to_friend * 1.2
    total_miles = miles_to_friend + miles_on_detour
    time_at_friends = 30
    total_time_away = total_miles / 44 + time_at_friends
    result = total_time_away
    
    return result

print(solution())