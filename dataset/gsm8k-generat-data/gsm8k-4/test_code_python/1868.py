def solution():
    """Alex and Max are running a race against each other. At the beginning of the race they are even with each other for 200 feet. Then Alex gets ahead of Max by 300 feet. Then Max gets ahead of Alex by 170 feet. Alex gets a burst of speed and gets ahead of Max by 440 feet. If the road they're running on is 5000 feet long, how many feet are there left for Max to catch up to Alex?"""
    # Define the initial distance between Alex and Max
    initial_distance = 200

    # Calculate the distance between Alex and Max after Alex gets ahead by 300 feet
    distance_after_alex300 = initial_distance + 300

    # Calculate the total distance covered by Alex and Max after Alex gets ahead by 300 feet
    total_distance_after_alex300 = initial_distance + 300 + 170

    # Calculate the distance between Alex and Max after Alex gets ahead by 440 feet
    distance_after_alex440 = total_distance_after_alex300 + 440

    # Calculate the distance remaining for Max to catch up to Alex
    distance_remaining = 5000 - distance_after_alex440

    result = distance_remaining
    return result

print(solution())