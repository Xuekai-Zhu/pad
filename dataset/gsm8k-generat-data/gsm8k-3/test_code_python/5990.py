def solution():
    """Oprah has 3500 cars in her collection. If the average number of cars she gives away per year is 50, how many years will it take to reduce her car collection to 500?"""

    # Define Oprah's initial number of cars and the target number of cars
    initial_cars = 3500
    target_cars = 500

    # Define the average number of cars Oprah gives away per year
    cars_given_away_per_year = 50

    # Calculate the number of years it will take Oprah to reduce her car collection to the target
    years = (initial_cars - target_cars)/cars_given_away_per_year

    # Display the number of years
    result = years
    return result

print(solution())