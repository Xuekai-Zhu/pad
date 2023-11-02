def solution():
    
    stanley_cups_per_hour = 4
    carl_cups_per_hour = 7
    hours = 3
    stanley_total_cups = stanley_cups_per_hour * hours
    carl_total_cups = carl_cups_per_hour * hours
    difference = carl_total_cups - stanley_total_cups
    result = difference
    return result

print(solution())