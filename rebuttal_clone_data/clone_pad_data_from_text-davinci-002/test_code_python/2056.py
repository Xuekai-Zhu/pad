def solution():
     number_of_walks = 2
     days_in_a_year = 360
     wipes_needed = number_of_walks * days_in_a_year
     result = wipes_needed / 120
 
     return result

print(solution())