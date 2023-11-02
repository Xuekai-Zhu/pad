def solution():
    # Calculate the number of Starbursts candies Penelope has
    mms = 25  # number of M&M candies Penelope has
    ratio = 5/3  # ratio of M&M candies to Starbursts candies
    starbursts = (mms/ratio) * (1/3)  # calculate the number of Starbursts candies using the ratio
    result = starbursts
    return result

print(solution())