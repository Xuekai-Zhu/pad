def solution():
    """At the Boisjoli farm, there is a chicken coop where 270 hens and 3 roosters live. Every morning, around 8 a.m., Ms. Mosel goes to collect the eggs because, every morning, each hen lays one. Then, after 1 hour of collection, she puts all these eggs in boxes of 6. It takes her another 40 minutes. Once all this is done, Ms. Mosel brings all the boxes of eggs to her village. She does it from Monday to Sunday, because chickens don't have a day off. How many boxes does Ms. Mosel fill each week?"""
    # Define the number of hens and roosters
    hens = 270
    roosters = 3

    # Calculate the number of eggs laid per day
    eggs_per_day = (hens + roosters) * 1

    # Calculate the number of eggs collected per week
    eggs_per_week = eggs_per_day * 7

    # Calculate the number of boxes filled per week
    boxes_per_week = eggs_per_week // 6

    result = boxes_per_week
    return result

print(solution())