def solution():
    """Eastern rattlesnakes have 6 segments in their tails, while Western rattlesnakes have 8 segments. What is the percentage difference in their tail size, expressed as a percentage of the Western rattlesnake's tail size?"""
    # Define the number of segments in each type of rattlesnake's tail
    EASTERN_SEGMENTS = 6
    WESTERN_SEGMENTS = 8

    # Calculate the percentage difference in tail size
    percentage_difference = ((WESTERN_SEGMENTS - EASTERN_SEGMENTS) / WESTERN_SEGMENTS) * 100

    # Display the percentage difference
    result = percentage_difference
    return result

print(solution())