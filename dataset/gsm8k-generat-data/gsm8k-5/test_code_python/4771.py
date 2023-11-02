def solution():
    car_rental_cost = 150  # John paid $150 to rent the car
    gas_price_per_gallon = 3.5  # Gas costs $3.50 per gallon
    gas_in_gallons = 8  # John bought 8 gallons of gas
    gas_cost = gas_price_per_gallon * gas_in_gallons  # John spent $28 on gas
    miles_driven = 320
    mileage_cost_per_mile = 0.5  # John paid $0.50 per mile
    mileage_cost = mileage_cost_per_mile * miles_driven  # John spent $160 on mileage

    # Calculate the total cost of the trip
    total_cost = car_rental_cost + gas_cost + mileage_cost
    result = total_cost
    return result

print(solution())