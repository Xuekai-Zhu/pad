def solution():
    total_distance = 5000  # The road they're running on is 5000 feet long
    initial_distance = 200  # At the beginning of the race they are even with each other for 200 feet
    distance_alex_ahead = 300  # Alex gets ahead of Max by 300 feet
    distance_max_ahead = 170  # Max gets ahead of Alex by 170 feet
    distance_alex_ahead_again = 440  # Alex gets ahead of Max by 440 feet

    # Calculate the distance Max is behind Alex after Alex gets ahead by 300 feet
    distance_max_behind_alex_1 = distance_alex_ahead - initial_distance

    # Calculate the distance Max is behind Alex after Max gets ahead by 170 feet
    distance_max_behind_alex_2 = distance_max_ahead + distance_max_behind_alex_1

    # Calculate the distance Max is behind Alex after Alex gets ahead by 440 feet
    distance_max_behind_alex_3 = distance_alex_ahead_again - distance_max_behind_alex_2

    # Calculate the distance Max needs to catch up to Alex
    distance_to_catch_up = total_distance - (initial_distance + distance_alex_ahead + distance_max_ahead + distance_alex_ahead_again)
    distance_to_catch_up += distance_max_behind_alex_3

    result = distance_to_catch_up
    return result

print(solution())