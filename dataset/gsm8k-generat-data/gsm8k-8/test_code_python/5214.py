def solution():
    # Define variables
    age_when_3x_dogs = 6
    num_dogs_when_6 = 90
    num_cars_after_10_years = 210

    # Calculate number of cars and dogs when Derek was 6
    num_cars_when_6 = num_dogs_when_6 / 3
    total_pets_when_6 = num_dogs_when_6 + num_cars_when_6

    # Calculate number of cars and dogs after 10 years
    num_cars_after_10_years = num_cars_after_10_years + num_cars_when_6
    num_dogs_after_10_years = total_pets_when_6 - num_cars_when_6 - num_cars_after_10_years

    # Calculate current number of dogs
    current_age = age_when_3x_dogs + 10
    current_num_dogs = num_dogs_after_10_years * (2/3)**(current_age/10)

    result = current_num_dogs
    return result

print(solution())