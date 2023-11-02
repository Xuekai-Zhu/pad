def solution():
    """Penelope has 5 M&M candies for every 3 Starbursts candies. If she has 25 M&M candies, how many Starbursts candies does she have?"""
    # Define the ratio of M&M candies to Starbursts candies
    mm_st_ratio = 5/3

    # Calculate the number of Starbursts candies based on the number of M&M candies
    mm_candies = 25
    st_candies = mm_candies / mm_st_ratio

    # Round the result to the nearest whole number
    result = round(st_candies)
    return result

print(solution())