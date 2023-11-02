def solution():
     daily_total = 800
     segments_eaten = 60 + (2 * 120)
     segments_needed = daily_total - segments_eaten
     millipedes_needed = segments_needed / 50
     result = millipedes_needed
     
     return result

print(solution())