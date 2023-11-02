def solution():
    """Mary and Ann are going sledding. Mary slides down a hill that's 630 feet long at a speed of 90 feet/minute. Ann slides down a hill that's 800 feet long at a rate of 40 feet/minute. How much longer does Ann's trip take than Mary?"""
    mary_distance = 630
    mary_speed = 90
    ann_distance = 800
    ann_speed = 40
    mary_time = mary_distance / mary_speed
    ann_time = ann_distance / ann_speed
    difference = ann_time - mary_time
    result = difference
    return result

print(solution())