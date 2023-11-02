def solution():
    
    rental_fee = 150
    mileage_cost = 0.5
    monday_miles = 620
    thursday_miles = 744
    total_miles = monday_miles + thursday_miles
    total_cost = rental_fee + (total_miles * mileage_cost)
    result = total_cost
    return result

print(solution())