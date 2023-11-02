def solution():
     cups_per_meal = 1.5
     meals_per_day = 3
     cups_per_pound = 2.25
     pounds_per_meal = cups_per_meal / cups_per_pound
     total_pounds = pounds_per_meal * meals_per_day * 2
     result = total_pounds
     return result

print(solution())