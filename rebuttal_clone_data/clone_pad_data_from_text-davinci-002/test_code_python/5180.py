def solution():
     total_kids = 2000
     soccer_campers = total_kids / 2
     morning_campers = soccer_campers / 4
     afternoon_campers = soccer_campers - morning_campers
     result = afternoon_campers
     return result

print(solution())