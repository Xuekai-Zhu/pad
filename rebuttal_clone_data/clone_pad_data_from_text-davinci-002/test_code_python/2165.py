def solution():
     pages_read = 149
     pages_left = 381 - pages_read
     pages_per_day = 20
     days = 7
     pages_to_be_read = pages_left - (pages_per_day * days)
     result = pages_to_be_read
     
     return result

print(solution())