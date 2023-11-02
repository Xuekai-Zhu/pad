def solution():
     apples = 9
     oranges = 5
     tangerines = 17
     oranges_taken = 2
     tangerines_taken = 10
     oranges_left = oranges - oranges_taken
     tangerines_left = tangerines - tangerines_taken
     difference = tangerines_left - oranges_left
     result = difference
     return result

print(solution())