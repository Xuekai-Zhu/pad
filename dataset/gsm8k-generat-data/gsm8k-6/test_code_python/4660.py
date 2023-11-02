def solution():
    # Calculate the total amount earned by Alex from the grocery delivery
    trips = 40
    earnings_per_trip = 1.5  # Alex charges $1.5 per trip
    total_earnings = trips * earnings_per_trip
    
    # Calculate the cost of the groceries that Alex delivered
    car_cost = 14600
    remaining_cost = car_cost - 14500 - (total_earnings * 0.05)
    result = remaining_cost
    return result

print(solution())