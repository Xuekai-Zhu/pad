def solution():
     percent_change = -2
     end_of_day_value = 8722
     percent_change_decimal = percent_change / 100
     change_in_value = end_of_day_value * percent_change_decimal
     morning_value = end_of_day_value + change_in_value
     result = morning_value
     
     return result

print(solution())