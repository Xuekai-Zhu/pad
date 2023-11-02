def solution():
     words_per_minute = 38
     words_needed = 4560
     minutes_needed = words_needed / words_per_minute
     hours_needed = minutes_needed / 60
     result = hours_needed
     return result

print(solution())