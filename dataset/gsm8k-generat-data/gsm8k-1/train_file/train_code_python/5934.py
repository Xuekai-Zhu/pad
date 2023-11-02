def solution():
    """Kim drives 30 miles to her friend's house. On the way back she has to take a detour that is 20% longer. She spends 30 minutes at her friend's house. She drives at a speed of 44 mph. How long did she spend away from home?"""
    distance_to_friend = 30
    detour_percent = 20
    detour_distance = distance_to_friend * (detour_percent / 100)
    total_distance = distance_to_friend + detour_distance
    time_driving = total_distance / 44
    time_away = time_driving * 2 + 0.5
    result = time_away * 60
    return result

print(solution())