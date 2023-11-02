def solution():
    cars_jared = 300
    percentage_difference = 15
    cars_ann = cars_jared * ((100 - percentage_difference) / 100)
    cars_alfred = cars_ann - 7
    total_cars = cars_jared + cars_ann + cars_alfred
    result = total_cars
    return result

print(solution())