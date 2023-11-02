def solution():
    """After tests in California, the total number of Coronavirus cases was recorded as 2000 positive cases on a particular day. The number of cases increased by 500 on the second day, with 50 recoveries. On the third day, the total number of new cases spiked to 1500 with 200 recoveries. What's the total number of positive cases after the third day?"""
    day_one = 2000
    day_two = day_one + 500 - 50
    day_three = day_two + 1500 - 200
    result = day_three
    return result

print(solution())