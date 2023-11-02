def solution():
    
    car_cost = 14600
    initial_savings = 14500
    trips = 40
    trip_fee = 1.5
    groceries_percentage = 0.05

    money_needed = car_cost - initial_savings
    total_groceries_cost = (money_needed - (trips * trip_fee)) / groceries_percentage
    result = total_groceries_cost
    return result

print(solution())