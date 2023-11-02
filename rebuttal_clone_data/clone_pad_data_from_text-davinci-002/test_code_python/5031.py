def solution():
     desk_time = 6
     conversation_time = 10
     sitting_time = desk_time - conversation_time
     walking_time = sitting_time / 9
     result = walking_time
     return result

print(solution())