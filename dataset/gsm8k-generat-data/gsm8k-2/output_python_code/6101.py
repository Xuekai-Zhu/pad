def solution():
    """Galileo is currently renting a car that costs $20 per month. He is planning to buy a brand new car that costs $30 per month. If Galileo will have to pay for the new car for a year, how much will be the difference if he gets the brand new car instead of renting a car?"""
    
    # Calculate cost of renting car for a year
    rent_cost = 20 * 12
    
    # Calculate cost of buying a new car for a year
    new_car_cost = 30 * 12
    
    # Calculate the difference
    difference = new_car_cost - rent_cost
    
    result = difference
    return result

print(solution())