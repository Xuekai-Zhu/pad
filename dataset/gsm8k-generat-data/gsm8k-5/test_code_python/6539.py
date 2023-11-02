def solution():
    total_cars = 5650000
    supplier1_cars = 1000000
    supplier2_cars = supplier1_cars + 500000
    supplier3_cars = supplier1_cars + supplier2_cars
    remaining_cars = total_cars - supplier1_cars - supplier2_cars - supplier3_cars

    supplier4_cars = remaining_cars / 2
    supplier5_cars = remaining_cars / 2

    result = (supplier4_cars, supplier5_cars)
    return result

print(solution())