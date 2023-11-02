def solution():
     total_practice_time = 2 * 60
     shooting_time = total_practice_time / 2
     running_time = 2 * shooting_time
     weightlifting_time = total_practice_time - shooting_time - running_time
     result = weightlifting_time
     return result

print(solution())