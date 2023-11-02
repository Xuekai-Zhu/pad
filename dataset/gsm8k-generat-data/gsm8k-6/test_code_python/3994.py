def solution():
    total_cars = 10 * 5  # total number of miniature racing cars
    cars_given_to_nephews = (1/5) * total_cars * 2  # number of cars given to both nephews
    cars_left_with_Tom = total_cars - cars_given_to_nephews  # number of cars left with Tom
    result = cars_left_with_Tom
    return result

print(solution())