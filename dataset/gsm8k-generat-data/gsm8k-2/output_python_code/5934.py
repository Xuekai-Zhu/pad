def solution():
    """Kim drives 30 miles to her friend's house. On the way back she has to take a detour that is 20% longer. She spends 30 minutes at her friend's house. She drives at a speed of 44 mph. How long did she spend away from home?"""
    distance_to_friend = 30
    detour_percentage = 0.2
    distance_back_home = distance_to_friend * (1 + detour_percentage)
    total_distance = distance_to_friend + distance_back_home
    speed = 44
    total_time = (total_distance / speed) * 60 + 30
    result = total_time
    return result

print(solution())