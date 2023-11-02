def solution():
    
    carrots_per_pound = 6
    bed_1_carrots = 55
    bed_2_carrots = 101
    bed_3_carrots = 78
    total_carrots = bed_1_carrots + bed_2_carrots + bed_3_carrots
    total_pounds = total_carrots / carrots_per_pound
    result = total_pounds
    return result

print(solution())