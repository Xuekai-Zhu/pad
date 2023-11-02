def solution():
    """Walter fell from the eighth platform of some scaffolding and fell past David after falling 4 meters. If he fell for an additional three more times that depth before hitting the ground, and the platforms are evenly spaced out in height, what platform was David on?"""
    fall_depth = 4
    additional_falls = 3
    total_fall_depth = fall_depth * (additional_falls + 1)
    walter_platform = 8
    david_platform = walter_platform - (total_fall_depth // fall_depth) - 1
    result = david_platform
    return result

print(solution())