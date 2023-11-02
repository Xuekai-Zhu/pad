def solution():
    minerals_yesterday = 48 - 6  # Joan had 6 fewer minerals yesterday
    gemstones_yesterday = minerals_yesterday / 2  # Joan had half as many gemstones as minerals yesterday
    total_gemstones = gemstones_yesterday + 6  # Joan found 6 more mineral samples today

    result = total_gemstones
    return result

print(solution())