def solution():
    """John rents a car to visit his family. It cost $150 to rent the car. He also had to buy 8 gallons of gas to fill it up and gas is $3.50 per gallon. The final expense is $.50 per mile. If he drove 320 miles how much did it cost?"""
    rental_cost = 150
    gallons_of_gas = 8
    cost_per_gallon_of_gas = 3.50
    gas_cost = gallons_of_gas * cost_per_gallon_of_gas
    miles_driven = 320
    cost_per_mile = 0.50
    mileage_cost = miles_driven * cost_per_mile
    total_cost = rental_cost + gas_cost + mileage_cost
    result = total_cost
    return result

print(solution())