def solution():
    """Joan collects rocks. In her collection of rock samples, she had half as many gemstones as minerals yesterday. Today, she went on a rock collecting trip and found 6 more mineral samples. If she has 48 minerals now, how many gemstone samples does she have?"""
    yesterday_minerals = 48 - 6  # After finding 6 more today
    yesterday_gemstones = yesterday_minerals / 2
    total_gemstones = yesterday_gemstones  # Assuming no new gemstone samples were found today
    result = total_gemstones
    return result

print(solution())