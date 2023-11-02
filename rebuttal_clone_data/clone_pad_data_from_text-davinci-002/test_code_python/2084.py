def solution():
    car_wheels = 4
    lawnmower_wheels = 2
    bike_wheels = 2
    tricycle_wheels = 3
    unicycle_wheels = 1
    total_wheels = car_wheels + lawnmower_wheels + (bike_wheels * 2) + tricycle_wheels + unicycle_wheels
    result = total_wheels
    return result

print(solution())