def solution():
    rent_cost = 20
    new_car_cost = 30
    months_in_year = 12

    # Calculate the total cost of renting a car for a year
    rent_total_cost = rent_cost * months_in_year

    # Calculate the total cost of buying a brand new car for a year
    new_car_total_cost = new_car_cost * months_in_year

    # Calculate the difference between the two options
    difference = new_car_total_cost - rent_total_cost
    result = difference
    return result

print(solution())