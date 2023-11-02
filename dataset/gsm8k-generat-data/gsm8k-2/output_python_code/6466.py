def solution():
    """The temperature in New York in June 2020 was 80 degrees. If the temperature in Miami on this day was 10 degrees hotter than the temperature in New York, and 25 degrees cooler than the temperature in San Diego, what was the average temperature for the three cities?"""
    NY_temp = 80
    Miami_temp = NY_temp + 10
    SD_temp = Miami_temp + 25
    avg_temp = (NY_temp + Miami_temp + SD_temp) / 3
    result = avg_temp
    return result

print(solution())