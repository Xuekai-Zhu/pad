def solution():
     point_total = 30 + 28 + 32 + 34 + 26
     number_of_games = 5
     average_points = point_total/number_of_games
     if average_points >= 30:
         salary = 10000
     else:
         salary = 8000
     result = salary
     return result

print(solution())