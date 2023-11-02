def solution():
    # Calculate the amount of fuel used in the second and third thirds of the trip
    fuel_second_thirds = (1/3) * 60  # a third of all of her fuel
    fuel_final_third = (1/2) * fuel_second_thirds  # half the amount of fuel used in the second third

    # Calculate the total amount of fuel used in the second and third thirds of the trip
    fuel_last_two_thirds = fuel_second_thirds + fuel_final_third

    # Calculate the amount of fuel used in the first third of the trip
    fuel_first_third = 60 - fuel_last_two_thirds

    result = fuel_first_third
    return result

print(solution())