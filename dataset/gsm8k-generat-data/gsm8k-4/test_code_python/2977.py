def solution():
    """Cindy can jump rope for 12 minutes before tripping up on the ropes. Betsy can jump rope half as long as Cindy before tripping up, while Tina can jump three times as long as Betsy. How many more minutes can Tina jump rope than Cindy?"""
    # Define Cindy's jump rope time
    cindy_time = 12

    # Calculate Betsy's jump rope time
    betsy_time = cindy_time / 2

    # Calculate Tina's jump rope time
    tina_time = betsy_time * 3

    # Calculate the difference between Tina's and Cindy's jump rope time
    time_difference = tina_time - cindy_time

    # Return the result
    result = time_difference
    return result

print(solution())