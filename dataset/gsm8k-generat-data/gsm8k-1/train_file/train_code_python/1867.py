def solution():
    """Alex and Max are running a race against each other. At the beginning of the race they are even with each other for 200 feet. Then Alex gets ahead of Max by 300 feet. Then Max gets ahead of Alex by 170 feet. Alex gets a burst of speed and gets ahead of Max by 440 feet. If the road they're running on is 5000 feet long, how many feet are there left for Max to catch up to Alex?"""
    total_distance = 5000
    distance_covered_by_alex = 200 + 300 + 440
    distance_left_for_alex = total_distance - distance_covered_by_alex
    distance_covered_by_max = distance_covered_by_alex - 170
    distance_left_for_max = distance_left_for_alex + distance_covered_by_max
    result = distance_left_for_max
    return result

print(solution())