def solution():
    """It was time for Kelly to harvest her carrots that she had planted in three different beds. In the first bed she pulled out 55 carrots. In the second bed she pulled out 101 carrots and in the third bed she pulled out 78 carrots. She found that 6 carrots weighed one pound. How many pounds of carrots did Kelly harvest?"""
    carrots_per_pound = 6
    bed_1_carrots = 55
    bed_2_carrots = 101
    bed_3_carrots = 78
    total_carrots = bed_1_carrots + bed_2_carrots + bed_3_carrots
    total_pounds = total_carrots / carrots_per_pound
    result = total_pounds
    return result

print(solution())