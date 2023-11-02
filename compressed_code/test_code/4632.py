def solution():
    
    current_cars = 3500
    cars_given_per_year = 50
    target_cars = 500
    years = 0
    while current_cars > target_cars:
        current_cars -= cars_given_per_year
        years += 1
    result = years
    return result

print(solution())