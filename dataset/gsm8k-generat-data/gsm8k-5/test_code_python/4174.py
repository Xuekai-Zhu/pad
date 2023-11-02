def solution():
    black_car_capacity = 4000  # each black car can hold 4000 pounds of coal
    blue_car_capacity = 2 * black_car_capacity  # each blue car can hold twice as much as black car
    red_car_capacity = 3 * blue_car_capacity  # each red car can hold three times as much as the blue car

    # Calculate the total capacity of all boxcars
    total_capacity = (3 * red_car_capacity) + (4 * blue_car_capacity) + (7 * black_car_capacity)
    result = total_capacity
    return result

print(solution())