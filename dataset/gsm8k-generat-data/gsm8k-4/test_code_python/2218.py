def solution():
    """Eastern rattlesnakes have 6 segments in their tails, while Western rattlesnakes have 8 segments. What is the percentage difference in their tail size, expressed as a percentage of the Western rattlesnake's tail size?"""
    # Define the number of segments in the tails of each type of rattlesnake
    eastern_segments = 6
    western_segments = 8

    # Calculate the percentage difference in tail size
    percentage_difference = ((western_segments - eastern_segments) / western_segments) * 100

    result = percentage_difference
    return result

print(solution())