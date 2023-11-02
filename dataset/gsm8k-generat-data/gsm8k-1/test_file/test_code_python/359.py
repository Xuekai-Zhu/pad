def solution():
    """John drives to his friend's house 200 miles away. He drives at a speed of 70 mph. He had to take a detour that added 10 miles to his trip. After he gets there he takes a route home that is 240 miles but he goes 80 mph. How long did the trip take?"""
    distance_to_friend = 200
    detour_distance = 10
    distance_home = 240
    speed_to_friend = 70
    speed_home = 80

    # Calculate time to get to friend's house (including detour)
    total_distance_to_friend = distance_to_friend + detour_distance
    time_to_friend = total_distance_to_friend / speed_to_friend

    # Calculate time to get home
    time_home = distance_home / speed_home

    # Calculate total trip time
    total_time = time_to_friend + time_home

    result = total_time
    return result

print(solution())