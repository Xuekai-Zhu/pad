def solution():
    """Elvis starts driving from his house and travels west for 5 hours. Then he turns around and travels east for 8 hours. If he was driving at an average speed of 18mph for both parts of the journey, how far is he from his house now?"""
    west_time = 5
    east_time = 8
    speed = 18
    west_distance = west_time * speed
    east_distance = east_time * speed
    total_distance = west_distance + east_distance
    result = total_distance
    return result

print(solution())