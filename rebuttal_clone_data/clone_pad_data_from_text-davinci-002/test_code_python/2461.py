def solution():
     value_lost_per_year = 1000
     initial_value = 20000
     number_of_years = 6
     total_value_lost = value_lost_per_year * number_of_years
     current_value = initial_value - total_value_lost
     result = current_value
     
     return result

print(solution())