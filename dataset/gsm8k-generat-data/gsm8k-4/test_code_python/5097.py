def solution():
    """Joan collects rocks. In her collection of rock samples, she had half as many gemstones as minerals yesterday. Today, she went on a rock collecting trip and found 6 more mineral samples. If she has 48 minerals now, how many gemstone samples does she have?"""
    # Calculate the initial number of minerals and gemstones
    initial_minerals = 48 - 6
    initial_gemstones = initial_minerals / 2

    # Calculate the current number of gemstones
    current_gemstones = initial_gemstones

    # return the result
    result = current_gemstones
    return result

print(solution())