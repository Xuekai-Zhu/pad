def solution():
    """Alex and Max are running a race against each other. At the beginning of the race they are even with each other for 200 feet. Then Alex gets ahead of Max by 300 feet. Then Max gets ahead of Alex by 170 feet. Alex gets a burst of speed and gets ahead of Max by 440 feet. If the road they're running on is 5000 feet long, how many feet are there left for Max to catch up to Alex?"""
    starting_distance = 200
    alex_leads_by_1 = starting_distance + 300
    max_leads_by_1 = alex_leads_by_1 - 170
    alex_leads_by_2 = max_leads_by_1 + 440
    total_distance = 5000
    max_distance_left = total_distance - alex_leads_by_2
    result = max_distance_left
    return result

print(solution())