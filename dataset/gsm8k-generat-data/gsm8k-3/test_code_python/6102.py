def solution():
    """Galileo is currently renting a car that costs $20 per month. He is planning to buy a brand new car that costs $30 per month. If Galileo will have to pay for the new car for a year, how much will be the difference if he gets the brand new car instead of renting a car?"""
    # Define the cost of renting and buying a car per month
    RENTAL_COST = 20
    BUYING_COST = 30

    # Calculate the total cost of renting a car for a year
    rental_cost_year = RENTAL_COST * 12

    # Calculate the total cost of buying a new car for a year
    buying_cost_year = BUYING_COST * 12

    # Calculate the difference in cost between renting and buying a car for a year
    difference = buying_cost_year - rental_cost_year

    # Display the difference in cost
    result = difference
    return result

print(solution())