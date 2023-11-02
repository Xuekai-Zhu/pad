def solution():
    # Calculate the total cost of the cabin rental, including pet fee and service/cleaning fee
    daily_rate = 125
    rental_days = 14
    rental_cost = daily_rate * rental_days
    pet_fee = 100
    service_fee = 0.2 * rental_cost
    total_cost = rental_cost + pet_fee + service_fee

    # Calculate the security deposit
    security_deposit = 0.5 * total_cost
    result = security_deposit
    return result

print(solution())