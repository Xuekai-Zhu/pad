def solution():
    """Lana and Mike are taking their dog and renting a cabin in the mountains for 2 weeks. The daily rate is $125.00 There is a $100.00 pet fee. There is also a 20% service/cleaning fee for the rental. They need to pay 50% of the entire bill as a security deposit. How much is their security deposit?"""
    # Define the daily rate and length of stay
    daily_rate = 125
    length_of_stay = 14

    # Define the pet fee and service/cleaning fee
    pet_fee = 100
    service_fee = 0.2

    # Calculate the total cost of the rental
    rental_cost = daily_rate * length_of_stay + pet_fee
    rental_cost_with_fee = rental_cost + rental_cost * service_fee

    # Calculate the security deposit required
    security_deposit = rental_cost_with_fee * 0.5

    # return the result
    result = security_deposit
    return result

print(solution())