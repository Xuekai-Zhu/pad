def solution():
    """Allie picked 44 wildflowers. Thirteen of the flowers were yellow and white, seventeen of the flowers were red and yellow, and 14 of the flowers were red and white. How many more flowers contained the color red than contained the color white?"""
    total_flowers = 44
    yellow_white = 13
    red_yellow = 17
    red_white = 14
    white = yellow_white + red_white - (total_flowers - red_yellow)
    red = total_flowers - white - yellow_white
    difference = red - white
    result = difference
    return result

print(solution())