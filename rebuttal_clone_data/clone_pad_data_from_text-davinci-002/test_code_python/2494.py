def solution():
    rocks_start_s = 837
    rocks_start_c = 723
    rocks_day1_s = 4
    rocks_day1_c = 8*rocks_day1_s
    rocks_day2_c = 123
    rocks_day3_s = 2*rocks_day1_s
    rocks_day3_c = rocks_start_c + rocks_day1_c + rocks_day2_c + rocks_day3_s
    result = rocks_day3_c
    return result

print(solution())