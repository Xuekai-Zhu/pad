def solution():
    """Lenny bought 20 boxes of pens. Each box contained 5 pens. She gave 40% of the pens to her close friends and one-fourth of what's left to her classmates. How many pens were left for Lenny?"""
    total_pens = 20 * 5
    friends_pens = 0.4 * total_pens
    remaining_pens = total_pens - friends_pens
    classmates_pens = remaining_pens / 4
    pens_left = remaining_pens - classmates_pens
    result = pens_left
    return result

print(solution())