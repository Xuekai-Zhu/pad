def solution():
    """Galileo is currently renting a car that costs $20 per month. He is planning to buy a brand new car that costs $30 per month. If Galileo will have to pay for the new car for a year, how much will be the difference if he gets the brand new car instead of renting a car?"""
    # Define the monthly rental fee and the monthly fee for the new car
    rental_fee = 20
    new_car_fee = 30

    # Calculate the total cost of renting the car for a year
    rental_cost = rental_fee * 12

    # Calculate the total cost of paying for the new car for a year
    new_car_cost = new_car_fee * 12

    # Calculate the difference in cost between renting and buying the new car
    cost_difference = new_car_cost - rental_cost

    # Return the result
    result = cost_difference
    return result

print(solution())