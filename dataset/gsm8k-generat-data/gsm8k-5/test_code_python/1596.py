def solution():
    distance_per_month = 400  # Nina tries to travel at least 400 kilometers in one month outside her home country
    every_second_month_distance = 2 * distance_per_month  # Nina travels twice that distance every second month
    months_per_year = 12  # There are 12 months in a year
    years = 2  # Nina wants to know how many kilometers she will travel in 2 years

    # Calculate the total distance Nina will travel in two years
    total_distance = (distance_per_month * months_per_year * years) + (every_second_month_distance * (years / 2))

    result = total_distance
    return result

print(solution())