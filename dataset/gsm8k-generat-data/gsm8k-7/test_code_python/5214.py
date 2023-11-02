def solution():
    num_dogs_6_years_old = 90
    age_6_years_old = 6

    # Calculate the number of cars when Derek was 6 years old
    num_cars_6_years_old = num_dogs_6_years_old / 3

    # Calculate the increase in the number of cars over 10 years
    increase_cars = 210

    # Calculate the decrease in the number of dogs over 10 years
    decrease_dogs = (num_dogs_6_years_old / 4) * 10

    # Calculate the current number of cars
    current_num_cars = num_cars_6_years_old + increase_cars - decrease_dogs

    # Calculate the current number of dogs
    current_num_dogs = (current_num_cars / 2) * 3
    result = current_num_dogs
    return result

print(solution())