def solution():
    """Walter fell from the eighth platform of some scaffolding and fell past David after falling 4 meters. If he fell for an additional three more times that depth before hitting the ground, and the platforms are evenly spaced out in height, what platform was David on?"""
    walter_fell_from = 8
    additional_fall_distance = 4 * 3
    david_platform = walter_fell_from - 1 - additional_fall_distance
    result = david_platform
    return result

print(solution())