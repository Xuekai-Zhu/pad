def solution():
    total_cars = 10 * 5  # 10 packages with 5 cars in each package
    cars_given = total_cars * (1/5) * 2  # Tom gave away 1/5 of the cars to each of his two nephews
    cars_left = total_cars - cars_given  # Calculate how many cars are left with Tom
    result = cars_left
    return result

print(solution())