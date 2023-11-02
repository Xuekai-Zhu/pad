def solution():
    oprah_cars = 3500
    cars_given_per_year = 50
    target_cars = 500

    years = (oprah_cars - target_cars) / cars_given_per_year
    result = years
    return result

print(solution())