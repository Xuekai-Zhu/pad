def solution():
    average_friday_13ths_per_year = 1
    friday_13ths_in_2015 = 3
    if friday_13ths_in_2015 > average_friday_13ths_per_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())