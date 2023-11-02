def solution():
    """Lana and Mike are taking their dog and renting a cabin in the mountains for 2 weeks.  The daily rate is $125.00  There is a $100.00 pet fee.  There is also a 20% service/cleaning fee for the rental.  They need to pay 50% of the entire bill as a security deposit.  How much is their security deposit?"""
    # Define the daily rate and fees
    DAILY_RATE = 125
    PET_FEE = 100
    SERVICE_FEE = 0.2

    # Calculate the total cost of the rental
    rental_cost = DAILY_RATE * 14 + PET_FEE
    service_cost = rental_cost * SERVICE_FEE
    total_cost = rental_cost + service_cost

    # Calculate the security deposit
    security_deposit = total_cost * 0.5

    # Display the security deposit
    result = security_deposit
    return result

print(solution())