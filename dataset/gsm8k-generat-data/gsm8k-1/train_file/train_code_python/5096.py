def solution():
    """Joan collects rocks. In her collection of rock samples, she had half as many gemstones as minerals yesterday. Today, she went on a rock collecting trip and found 6 more mineral samples. If she has 48 minerals now, how many gemstone samples does she have?"""
    minerals_yesterday = 48 - 6
    gemstones_yesterday = minerals_yesterday / 2
    gemstones_now = gemstones_yesterday
    result = gemstones_now
    return result

print(solution())