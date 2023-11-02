def solution():
     frogs_eaten_per_day = 9 * 15
     flies_eaten_per_day = frogs_eaten_per_day * 8
     total_flies_eaten_per_day = flies_eaten_per_day + (frogs_eaten_per_day * 30)
     result = total_flies_eaten_per_day
     return result

print(solution())