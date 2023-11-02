def solution():
     snow_first_day = .5
     snow_second_day = 8
     snow_melted_days1and2 = 4
     snow_fifth_day = snow_first_day * 2
     snow_now = snow_first_day + snow_second_day + snow_fifth_day - snow_melted_days1and2
     result = snow_now
     return result

print(solution())