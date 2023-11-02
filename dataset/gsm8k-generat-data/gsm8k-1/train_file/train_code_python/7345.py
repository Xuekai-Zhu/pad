def solution():
    """Penelope has 5 M&M candies for every 3 Starbursts candies. If she has 25 M&M candies, how many Starbursts candies does she have?"""
    mms_per_starbursts = 5/3
    mms_candies = 25
    starbursts_candies = mms_candies / mms_per_starbursts
    result = starbursts_candies
    return result

print(solution())