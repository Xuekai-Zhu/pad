def solution():
    """Lenny bought 20 boxes of pens. Each box contained 5 pens. She gave 40% of the pens to her close friends and one-fourth of what's left to her classmates. How many pens were left for Lenny?"""
    total_pens = 20 * 5
    pens_given_friends = int(total_pens * 0.4)
    pens_left = total_pens - pens_given_friends
    pens_given_classmates = pens_left // 4
    pens_left -= pens_given_classmates
    result = pens_left
    return result

print(solution())