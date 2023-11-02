def solution():
     minutes = 2
     seconds_per_minute = 60
     seconds_per_sneeze = 3
     total_seconds = minutes * seconds_per_minute
     total_sneezes = total_seconds / seconds_per_sneeze
     result = total_sneezes
     return result

print(solution())