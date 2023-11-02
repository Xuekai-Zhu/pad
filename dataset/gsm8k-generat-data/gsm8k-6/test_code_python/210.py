def solution():
    cars = 16
    for i in range(3):
        cars = cars + (0.5 * cars)  # Number of cars increases by 50% every year
    result = cars
    return result

print(solution())