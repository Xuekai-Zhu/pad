def solution():
    """Alex and Max are running a race against each other. At the beginning of the race they are even with each other for 200 feet. Then Alex gets ahead of Max by 300 feet. Then Max gets ahead of Alex by 170 feet. Alex gets a burst of speed and gets ahead of Max by 440 feet. If the road they're running on is 5000 feet long, how many feet are there left for Max to catch up to Alex?"""
    # Define the initial distance between Alex and Max
    initial_distance = 200

    # Calculate the distances between Alex and Max at different points in the race
    distance_after_alex_leads = initial_distance + 300
    distance_after_max_leads = distance_after_alex_leads - 170
    distance_after_alex_burst = distance_after_max_leads + 440

    # Calculate the distance remaining for Max to catch up to Alex
    remaining_distance = 5000 - distance_after_alex_burst

    # Display the remaining distance
    result = remaining_distance
    return result

print(solution())