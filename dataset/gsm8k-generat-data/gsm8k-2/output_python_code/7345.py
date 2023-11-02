def solution():
    """Penelope has 5 M&M candies for every 3 Starbursts candies. If she has 25 M&M candies, how many Starbursts candies does she have?"""
    mms = 25
    ratio = 5 / 3
    starbursts = (mms / ratio) - mms
    result = starbursts
    return result

print(solution())