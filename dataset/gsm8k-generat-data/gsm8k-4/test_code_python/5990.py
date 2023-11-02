def solution():
    """Oprah has 3500 cars in her collection. If the average number of cars she gives away per year is 50, how many years will it take to reduce her car collection to 500?"""
    # Define the initial number of cars and the target number of cars
    initial_cars = 3500
    target_cars = 500

    # Define the average number of cars given away per year
    cars_given_away_per_year = 50

    # Initialize the year counter
    years = 0

    # Calculate the number of years it will take to reach the target number of cars
    while initial_cars > target_cars:
        initial_cars -= cars_given_away_per_year
        years += 1

    # Display the result
    result = years
    return result

print(solution())