def solution():
    mary_length = 630
    mary_rate = 90
    ann_length = 800
    ann_rate = 40
    mary_time = mary_length / mary_rate
    ann_time = ann_length / ann_rate
    time_difference = ann_time - mary_time
    result = time_difference
    return result

print(solution())