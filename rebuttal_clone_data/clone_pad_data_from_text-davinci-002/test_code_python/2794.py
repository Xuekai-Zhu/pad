def solution():
     cars = 5
     fast_cars = 3
     fast_time = 40
     slow_cars = cars - fast_cars
     slow_time = fast_time * 1.5
     money_earned = (fast_cars * fast_time + slow_cars * slow_time) * 20
     result = money_earned
     return result

print(solution())