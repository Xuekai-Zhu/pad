def solution():
     total_students = 140
     dancers = total_students * 0.25 
     slow_dancers= dancers * 0.25 
     non_slow_dancers = dancers - slow_dancers
     return non_slow_dancers

print(solution())