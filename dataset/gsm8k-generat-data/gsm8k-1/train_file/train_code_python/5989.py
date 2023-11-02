def solution():
    """Oprah has 3500 cars in her collection. If the average number of cars she gives away per year is 50, how many years will it take to reduce her car collection to 500?"""
    starting_cars = 3500
    cars_given_away_per_year = 50
    final_cars = 500
    years_to_reduce = (starting_cars - final_cars) / cars_given_away_per_year
    result = years_to_reduce
    return result

print(solution())