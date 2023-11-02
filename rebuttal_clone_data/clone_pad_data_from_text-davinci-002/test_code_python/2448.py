def solution():
     boxes = 10
     bottles_per_box = 50
     capacity = 12
     filled_to = 3/4
     total_liters = (boxes * bottles_per_box * capacity * filled_to)
     result = total_liters

     return result

print(solution())