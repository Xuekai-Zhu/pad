def solution():
    cindy_time = 12  # Cindy can jump rope for 12 minutes before tripping up
    betsy_time = cindy_time / 2  # Betsy can jump rope half as long as Cindy before tripping up
    tina_time = betsy_time * 3  # Tina can jump rope three times as long as Betsy

    # Calculate the difference between Tina's and Cindy's jump rope times
    diff = tina_time - cindy_time
    result = diff
    return result

print(solution())