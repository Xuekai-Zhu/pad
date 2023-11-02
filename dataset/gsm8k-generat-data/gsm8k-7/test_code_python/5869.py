def solution():
    starting_cars = 14
    bought_cars = 28
    birthday_cars = 12
    given_to_sister = 8
    given_to_vinnie = 3

    # Calculate the total number of toy cars Jaden had after buying and receiving more
    total_cars = starting_cars + bought_cars + birthday_cars

    # Calculate the total number of cars given away
    given_away = given_to_sister + given_to_vinnie

    # Calculate the final number of toy cars Jaden has
    final_cars = total_cars - given_away
    result = final_cars
    return result

print(solution())