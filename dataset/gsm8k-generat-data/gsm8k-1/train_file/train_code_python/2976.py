def solution():
    """Cindy can jump rope for 12 minutes before tripping up on the ropes. Betsy can jump rope half as long as Cindy before tripping up, while Tina can jump three times as long as Betsy. How many more minutes can Tina jump rope than Cindy?"""
    cindy_time = 12
    betsy_time = cindy_time / 2
    tina_time = betsy_time * 3
    difference = tina_time - cindy_time
    result = difference
    return result

print(solution())