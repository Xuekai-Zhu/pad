def solution():
    initial_number_of_plants = 30
    number_of_plants_eaten_first_day = 20
    number_of_plants_eaten_second_day = 10
    number_of_plants_eaten_third_day = 1
    total_number_of_plants_eaten = number_of_plants_eaten_first_day + number_of_plants_eaten_second_day + number_of_plants_eaten_third_day
    remaining_plants = initial_number_of_plants - total_number_of_plants_eaten
    result = remaining_plants
    return result

print(solution())