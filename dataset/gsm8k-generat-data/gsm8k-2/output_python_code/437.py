def solution():
    """While Greg was camping with his family for a week, it rained for 3 days. When he looked at the weather records, he saw that the amount of rain was 3 mm, 6 mm, and 5 mm on the three days. During the same week, it rained 26 mm at his house. How much less rain did Greg experience while camping?"""
    camping_rain = 3 + 6 + 5
    house_rain = 26
    difference = house_rain - camping_rain
    result = difference
    return result

print(solution())