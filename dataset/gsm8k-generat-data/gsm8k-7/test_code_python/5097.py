def solution():
    num_minerals_yesterday = 48 - 6 # subtract the 6 new minerals found today
    num_gemstones_yesterday = num_minerals_yesterday / 2 # half as many gemstones as minerals
    num_gemstones_now = num_gemstones_yesterday # assuming no new gemstones were found today
    result = num_gemstones_now
    return result

print(solution())