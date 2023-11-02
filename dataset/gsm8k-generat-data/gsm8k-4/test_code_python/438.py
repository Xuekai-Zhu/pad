def solution():
    """While Greg was camping with his family for a week, it rained for 3 days. When he looked at the weather records, he saw that the amount of rain was 3 mm, 6 mm, and 5 mm on the three days. During the same week, it rained 26 mm at his house. How much less rain did Greg experience while camping?"""
    # Calculate the total amount of rain during the camping trip
    camping_rain = sum([3, 6, 5])

    # Calculate the difference between the camping rain and the amount of rain at Greg's house
    difference = 26 - camping_rain

    # Return the result
    result = difference
    return result

print(solution())