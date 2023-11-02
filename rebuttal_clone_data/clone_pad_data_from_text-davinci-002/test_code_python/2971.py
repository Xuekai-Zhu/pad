def solution():
     flies_eaten_per_day = 2
     flies_in_bottle_morning = 5
     flies_in_bottle_afternoon = 6
     flies_needed_per_week = flies_eaten_per_day * 7
     flies_gathered = flies_in_bottle_morning + flies_in_bottle_afternoon - 1
     flies_needed = flies_needed_per_week - flies_gathered
     result = flies_needed
     
     return result

print(solution())