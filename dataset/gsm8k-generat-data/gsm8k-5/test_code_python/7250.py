def solution():
    number_of_cars = 10  # The guests arrive in 10 cars
    wheels_per_car = 4  # Each car has 4 wheels
    dylans_parent_cars = 2  # Dylan's parents have their own cars in the parking lot

    # Calculate the total number of car wheels in the parking lot
    total_wheels = number_of_cars * wheels_per_car + dylans_parent_cars * wheels_per_car
    result = total_wheels
    return result

print(solution())