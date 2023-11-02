def solution():
    starting_cars = 3500
    cars_given_per_year = 50
    target_cars = 500

    # Calculate the total number of years it will take to reduce the car collection
    years = (starting_cars - target_cars) / cars_given_per_year
    result = years
    return result

print(solution())