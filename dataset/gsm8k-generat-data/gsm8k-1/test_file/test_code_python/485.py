def solution():
    """The highest temperature ever recorded in Southlandia is -48 degrees Fahrenheit. The highest temperature ever recorded in Northlandia is 21 degrees Fahrenheit. The highest temperature recorded in Midlandia is -3 degrees Fahrenheit. What is the average highest temperature of these 3 countries?"""
    southlandia_temp = -48
    northlandia_temp = 21
    midlandia_temp = -3
    sum_temp = southlandia_temp + northlandia_temp + midlandia_temp
    avg_temp = sum_temp / 3
    result = avg_temp
    return result

print(solution())