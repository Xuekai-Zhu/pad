def solution():
    daily_rate = 125  # The daily rate for the cabin is $125
    pet_fee = 100  # There is a $100 pet fee
    rental_duration = 14  # They are renting the cabin for 2 weeks

    # Calculate the total rental cost before the service/cleaning fee
    rental_cost = (daily_rate * rental_duration) + pet_fee

    # Calculate the service/cleaning fee
    service_fee = rental_cost * 0.2

    # Calculate the total rental cost with the service/cleaning fee included
    total_cost = rental_cost + service_fee

    # Calculate the security deposit required (50% of the total cost)
    security_deposit = total_cost * 0.5
    result = security_deposit
    return result

print(solution())