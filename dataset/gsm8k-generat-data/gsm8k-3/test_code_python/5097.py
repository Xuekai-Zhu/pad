def solution():
    """Joan collects rocks. In her collection of rock samples, she had half as many gemstones as minerals yesterday. Today, she went on a rock collecting trip and found 6 more mineral samples. If she has 48 minerals now, how many gemstone samples does she have?"""
    # Calculate the number of minerals Joan had yesterday
    minerals_yesterday = 48 - 6

    # Calculate the number of gemstones Joan had yesterday
    gemstones_yesterday = minerals_yesterday / 2

    # Calculate the number of gemstones Joan has now
    gemstones_now = gemstones_yesterday

    # Display the number of gemstones Joan has now
    result = gemstones_now
    return result

print(solution())