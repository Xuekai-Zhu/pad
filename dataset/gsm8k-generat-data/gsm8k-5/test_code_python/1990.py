def solution():
    # Calculate the manufacturing year of the second car
    year_second_car = 1970 + 10  # First car was manufactured 10 years earlier than the second car

    # Calculate the manufacturing year of the third car
    year_third_car = year_second_car + 20  # Third car was manufactured 20 years later than the second car

    result = year_third_car
    return result

print(solution())