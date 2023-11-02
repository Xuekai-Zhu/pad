def solution():
    """At the Boisjoli farm, there is a chicken coop where 270 hens and 3 roosters live. Every morning, around 8 a.m., Ms. Mosel goes to collect the eggs because, every morning, each hen lays one. Then, after 1 hour of collection, she puts all these eggs in boxes of 6. It takes her another 40 minutes. Once all this is done, Ms. Mosel brings all the boxes of eggs to her village. She does it from Monday to Sunday, because chickens don't have a day off. How many boxes does Ms. Mosel fill each week?"""
    hens = 270
    roosters = 3
    total_birds = hens + roosters
    eggs_per_day = total_birds
    boxes_per_day = eggs_per_day // 6
    days_per_week = 7
    total_boxes = boxes_per_day * days_per_week
    result = total_boxes
    return result

print(solution())