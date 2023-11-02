def solution():
    total_cars = 3000  # There are 3000 cars at the dealership

    # Calculate the number of cars that cost less than $15000
    less_than_15 = int(total_cars * 0.15)

    # Calculate the number of cars that cost more than $20000
    more_than_20 = int(total_cars * 0.40)

    # Calculate the number of cars that cost between $15000 and $20000
    between_15_and_20 = total_cars - less_than_15 - more_than_20
    result = between_15_and_20
    return result

print(solution())