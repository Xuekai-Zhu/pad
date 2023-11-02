def solution():
     hours_in_class = 18
     hours_homework = 4
     hours_sleeping = 8
     hours_working = 20
     hours_leftover = 24 - (hours_in_class + hours_homework + hours_sleeping + hours_working) 
     result = hours_leftover
     return result

print(solution())