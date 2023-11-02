def solution():
    
    savings = 14500
    car_cost = 14600
    trips = 40
    fee_per_trip = 1.5
    fee_percent = 0.05
    total_fees = trips * fee_per_trip
    groceries = (car_cost - savings - total_fees)/(fee_percent)
    result = groceries
    return result

print(solution())