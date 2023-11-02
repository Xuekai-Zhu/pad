def solution():
    daily_rate = 125.0
    num_weeks = 2
    pet_fee = 100.0
    service_fee = 0.2  # 20% service/cleaning fee

    # Calculate the total cost of the cabin rental for 2 weeks
    total_rental_cost = (daily_rate * 7 * num_weeks) + pet_fee

    # Calculate the service/cleaning fee
    total_service_fee = total_rental_cost * service_fee

    # Add the service/cleaning fee to the rental cost to get the total cost
    total_cost = total_rental_cost + total_service_fee

    # Calculate the security deposit, which is 50% of the total cost
    security_deposit = 0.5 * total_cost
    result = security_deposit
    return result

print(solution())