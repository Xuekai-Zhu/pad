def solution():
    # Calculate the total rental fee for the cabin
    daily_rate = 125.00
    rental_days = 14
    rental_fee = daily_rate * rental_days

    # Add the pet fee to the rental fee
    pet_fee = 100.00
    total_fee = rental_fee + pet_fee

    # Calculate the service/cleaning fee for the rental
    service_fee = total_fee * 0.20

    # Add the service/cleaning fee to the total fee
    total_fee_with_service_fee = total_fee + service_fee

    # Calculate the security deposit
    security_deposit = total_fee_with_service_fee * 0.50
    result = security_deposit
    return result

print(solution())