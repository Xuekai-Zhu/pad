def solution():
    initial_speed = 20
    speed_incline = 12
    speed_decline = 24
    hours_incline = 4.5
    hours_decline = 2.5
    hours_puncture = 1.5
    total_hours = hours_incline + hours_decline + hours_puncture
    initial_distance = initial_speed * hours_incline
    incline_distance = hours_incline * speed_incline
    decline_distance = hours_decline * speed_decline
    total_distance = initial_distance + incline_distance + decline_distance
    distance_to_town = 164
    distance_walked = distance_to_town - total_distance
    result = distance_walked
    
    return result

print(solution())