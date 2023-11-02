def solution():
     growth_rate = 2
     current_height = 10
     weeks_in_a_month = 4
     number_of_months = 4
     total_growth = growth_rate * weeks_in_a_month * number_of_months
     total_height = current_height + total_growth
     result = total_height
     return result

print(solution())