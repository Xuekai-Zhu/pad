def solution():
    """As Sally walked to school, she was holding the strings to 25 red balloons, 7 green balloons, and 12 yellow balloons. Suddenly, a gust of wind caused 40% of the red balloons to burst. The shockingly loud sound startled Sally, and she accidentally released half of the yellow balloons. But as she neared the school grounds, she found 8 blue balloons caught in a tree, and she added 75% of them to her remaining clutch of balloons, which she carried into the school. What number of balloons did she finally carry into the school?"""
    red_balloons = 25
    green_balloons = 7
    yellow_balloons = 12
    burst_red_balloons = red_balloons * 0.4
    remaining_red_balloons = red_balloons - burst_red_balloons
    remaining_yellow_balloons = yellow_balloons / 2
    blue_balloons = 8
    added_blue_balloons = blue_balloons * 0.75
    remaining_balloons = remaining_red_balloons + green_balloons + remaining_yellow_balloons
    final_balloons = remaining_balloons + added_blue_balloons
    result = final_balloons
    return result

print(solution())