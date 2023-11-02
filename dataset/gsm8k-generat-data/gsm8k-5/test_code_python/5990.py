def solution():
    oprah_cars = 3500  # Oprah has 3500 cars in her collection
    cars_given_away_per_year = 50  # Oprah gives away an average of 50 cars per year
    desired_cars = 500  # Oprah wants to reduce her collection to 500 cars

    # Calculate the number of years it will take to reduce the car collection to 500
    years_to_reduce = (oprah_cars - desired_cars) / cars_given_away_per_year
    result = years_to_reduce
    return result

print(solution())