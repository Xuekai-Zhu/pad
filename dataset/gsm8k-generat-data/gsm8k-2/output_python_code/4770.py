def solution():
    """John rents a car to visit his family. It cost $150 to rent the car. He also had to buy 8 gallons of gas to fill it up and gas is $3.50 per gallon. The final expense is $.50 per mile. If he drove 320 miles how much did it cost?"""
    car_rental_cost = 150
    gas_cost = 8 * 3.5
    mileage_cost = 320 * 0.5
    total_cost = car_rental_cost + gas_cost + mileage_cost
    result = total_cost
    return result

print(solution())