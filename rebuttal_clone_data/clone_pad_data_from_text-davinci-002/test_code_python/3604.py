def solution():
     first_week = 40
     second_week = 2 * first_week
     third_week = (1 - 0.7) * (first_week + second_week)
     result = third_week
     return result

print(solution())