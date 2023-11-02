def solution():
     carrots_first_bed = 55
     carrots_second_bed = 101
     carrots_third_bed = 78
     carrots_per_pound = 6
     total_carrots = carrots_first_bed + carrots_second_bed + carrots_third_bed
     total_pounds = total_carrots / carrots_per_pound
     result = total_pounds
     return result

print(solution())