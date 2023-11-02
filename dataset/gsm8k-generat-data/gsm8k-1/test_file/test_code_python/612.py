def solution():
    """Jane planted a beanstalk in her backyard. After the first week, it was 3 inches tall. It doubled in height the second week. It grew another 4 inches in the third week. How tall was the beanstalk after 3 weeks?"""
    height_first_week = 3
    height_second_week = height_first_week * 2
    height_third_week = height_second_week + 4
    total_height = height_first_week + height_second_week + height_third_week
    result = total_height
    return result

print(solution())