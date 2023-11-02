def solution():
    Stanley_cups_per_hour = 4
    Carl_cups_per_hour = 7
    hours = 3
    Stanley_total_cups = Stanley_cups_per_hour * hours
    Carl_total_cups = Carl_cups_per_hour * hours
    difference = Carl_total_cups - Stanley_total_cups
    result = difference
    return result

print(solution())