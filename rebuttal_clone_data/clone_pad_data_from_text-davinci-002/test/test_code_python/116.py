def solution():
    
    initial_cars = 16
    percent_increase = 50
    cars_after_one_year = initial_cars + (initial_cars * (percent_increase / 100))
    cars_after_two_years = cars_after_one_year + (cars_after_one_year * (percent_increase / 100))
    cars_after_three_years = cars_after_two_years + (cars_after_two_years * (percent_increase / 100))
    result = cars_after_three_years
    return result

print(solution())