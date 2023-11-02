def solution():
     drink_one_size = 12
     drink_one_caffeine = 250
     drink_two_size = 2
     drink_two_caffeine = drink_one_caffeine * 3
     pill_caffeine = (drink_one_size * drink_one_caffeine) + (drink_two_size * drink_two_caffeine)
     
     result = pill_caffeine
     return result

print(solution())